import requests
from bs4 import BeautifulSoup
from .base import BaseScraper

class BeautifulSoupAdapter(BaseScraper):
    """
    Static HTML scraper using Requests and BeautifulSoup.
    Extremely fast, best used for standard static university directories.
    """
    
    def __init__(self, headers=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
    def fetch(self, url):
        response = requests.get(url, headers=self.headers, timeout=30)
        response.raise_for_status()
        return response.text
        
    def parse(self, raw_data):
        soup = BeautifulSoup(raw_data, 'lxml')
        # This should be implemented by the specific child class
        # Example dummy implementation:
        items = []
        for row in soup.find_all('div', class_='faculty-member'):
            items.append({
                'name': row.find('h3').text.strip() if row.find('h3') else '',
                'title': row.find('span', class_='title').text.strip() if row.find('span', class_='title') else '',
            })
        return items
        
    def normalize(self, parsed_item):
        # Specific normalization logic
        if not parsed_item.get('name'):
            return None
        return parsed_item
