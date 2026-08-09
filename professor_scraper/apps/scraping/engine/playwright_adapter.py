from playwright.sync_api import sync_playwright
from .base import BaseScraper

class PlaywrightAdapter(BaseScraper):
    """
    Next-generation dynamic scraper using Playwright.
    Best for extremely fast JS-rendered pages, handling network interception, and avoiding bot detection.
    """
    
    def __init__(self, headless=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headless = headless
        
    def fetch(self, url):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            context = browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            )
            page = context.new_page()
            
            # Optional: Block images/fonts to speed up scraping
            page.route("**/*", lambda route: route.continue_() if route.request.resource_type in ["document", "script", "fetch", "xhr"] else route.abort())
            
            page.goto(url, wait_until="networkidle")
            
            # Extract content
            html_content = page.content()
            
            context.close()
            browser.close()
            return html_content
            
    def parse(self, raw_data):
        # Parsing logic (can also use Playwright locators inside fetch, but returning HTML is standard)
        return [{"status": "success", "length": len(raw_data)}]
        
    def normalize(self, parsed_item):
        return parsed_item
