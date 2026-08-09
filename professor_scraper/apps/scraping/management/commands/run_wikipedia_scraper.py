import logging
from django.core.management.base import BaseCommand
from apps.scraping.engine.bs4_adapter import BeautifulSoupAdapter
from apps.countries.models import Country, City
from apps.universities.models import University
from django.utils.text import slugify
from bs4 import BeautifulSoup
import uuid

logger = logging.getLogger(__name__)

class WikipediaUniversityScraper(BeautifulSoupAdapter):
    """
    Concrete scraper implementation to collect Universities from Wikipedia
    and map them perfectly to our database schema.
    """
    
    def parse(self, raw_data):
        soup = BeautifulSoup(raw_data, 'lxml')
        items = []
        
        # Look for the main tables in wikipedia lists
        tables = soup.find_all('table', class_='wikitable')
        for table in tables:
            rows = table.find_all('tr')[1:] # Skip header
            for row in rows:
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 2:
                    name_tag = cols[0].find('a')
                    name = name_tag.text.strip() if name_tag else cols[0].text.strip()
                    
                    # Usually column 2 or 3 is the location
                    location_tag = cols[1].find('a')
                    city_name = location_tag.text.strip() if location_tag else cols[1].text.strip()
                    
                    if name and len(name) > 3 and not name.isnumeric():
                        items.append({
                            'name': name[:250],
                            'city': city_name[:250],
                            'country': 'Canada', # Hardcoded for this specific URL example
                            'url': f"https://en.wikipedia.org{name_tag['href']}" if name_tag and name_tag.has_attr('href') else ''
                        })
        return items

    def normalize(self, parsed_item):
        try:
            # 1. Get or Create Country
            country, _ = Country.objects.get_or_create(
                name=parsed_item['country'],
                defaults={'iso_code': 'CA', 'continent': 'North America'}
            )
            
            # 2. Get or Create City
            city, _ = City.objects.get_or_create(
                name=parsed_item['city'],
                country=country,
                defaults={'region': ''}
            )
            
            # 3. Create or Update University
            # Ensure slug is unique if it exists
            university_slug = slugify(parsed_item['name'])
            
            # We use try/except for IntegrityError handling in production,
            # but for this script we assume canonical_name is unique.
            university, created = University.objects.update_or_create(
                canonical_name=parsed_item['name'],
                defaults={
                    'slug': university_slug[:250] if university_slug else str(uuid.uuid4()),
                    'country': country,
                    'city': city,
                    'official_website': parsed_item['url'][:500],
                    'verification_status': 'SCRAPED',
                }
            )
            
            return {
                'status': 'created' if created else 'updated',
                'university': university.canonical_name
            }
            
        except Exception as e:
            logger.error(f"Error normalizing {parsed_item.get('name')}: {e}")
            return None


class Command(BaseCommand):
    help = 'Run the Wikipedia University Scraper to populate the database.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting Wikipedia Scraper..."))
        
        target_url = "https://en.wikipedia.org/wiki/List_of_universities_in_Canada"
        
        scraper = WikipediaUniversityScraper()
        results = scraper.run(target_url)
        
        created_count = sum(1 for r in results if r and r.get('status') == 'created')
        updated_count = sum(1 for r in results if r and r.get('status') == 'updated')
        
        self.stdout.write(self.style.SUCCESS(f"Successfully scraped {len(results)} records!"))
        self.stdout.write(f"Created: {created_count}")
        self.stdout.write(f"Updated: {updated_count}")
