from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

class BaseScraper(ABC):
    """
    The Base Interface for all scrapers in the Global Academic Intelligence Platform.
    Enforces a strict lifecycle: Initialize -> Fetch -> Parse -> Normalize -> Save.
    """
    
    def __init__(self, job_id=None):
        self.job_id = job_id
        self.results = []
        
    @abstractmethod
    def fetch(self, url):
        """Fetch raw data (HTML, JSON, etc.) from the source."""
        pass
        
    @abstractmethod
    def parse(self, raw_data):
        """Extract structured entities from the raw data."""
        pass
        
    @abstractmethod
    def normalize(self, parsed_item):
        """Transform parsed data to match the Django Database Schema."""
        pass
        
    def save(self, normalized_item):
        """Save normalized data to the database or queue for review."""
        # This will interface with Django models directly or via API.
        # For now, we append to results.
        self.results.append(normalized_item)
        return True

    def run(self, url):
        """Execute the full scraping pipeline."""
        try:
            logger.info(f"[{self.__class__.__name__}] Starting scrape for {url}")
            raw = self.fetch(url)
            items = self.parse(raw)
            
            for item in items:
                normalized = self.normalize(item)
                if normalized:
                    self.save(normalized)
                    
            logger.info(f"[{self.__class__.__name__}] Completed. Scraped {len(self.results)} items.")
            return self.results
            
        except Exception as e:
            logger.error(f"Scraper failed: {str(e)}", exc_info=True)
            raise
