from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base import BaseScraper
import time

class SeleniumAdapter(BaseScraper):
    """
    Dynamic HTML scraper using Selenium.
    Best for complex single-page apps (SPAs) or sites requiring clicks/logins.
    """
    
    def __init__(self, headless=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.options = Options()
        if headless:
            self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        
    def fetch(self, url):
        driver = webdriver.Chrome(options=self.options)
        try:
            driver.get(url)
            # Wait for specific element to load - override in child class
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            # Optional: handle infinite scrolling or pagination here
            time.sleep(2) 
            return driver.page_source
        finally:
            driver.quit()
            
    def parse(self, raw_data):
        # Usually parse with BeautifulSoup after fetching with Selenium
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(raw_data, 'html.parser')
        return [{"raw_html": str(soup.title)}]
        
    def normalize(self, parsed_item):
        return parsed_item
