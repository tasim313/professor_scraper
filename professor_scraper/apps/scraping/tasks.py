import os
from celery import shared_task
from django.utils import timezone
from .models import ScraperJob, ScraperResult
from .engine.bs4_adapter import BeautifulSoupAdapter
from .engine.playwright_adapter import PlaywrightAdapter
from .engine.selenium_adapter import SeleniumAdapter
import logging

logger = logging.getLogger(__name__)

@shared_task
def execute_scraping_job(job_id, target_url, adapter_type='bs4'):
    """
    Celery task to run a scraper asynchronously.
    adapter_type: 'bs4', 'selenium', or 'playwright'
    """
    try:
        job = ScraperJob.objects.get(id=job_id)
        job.status = 'RUNNING'
        job.started_at = timezone.now()
        job.save()
        
        # Select Engine
        if adapter_type == 'playwright':
            scraper = PlaywrightAdapter(job_id=job.id)
        elif adapter_type == 'selenium':
            scraper = SeleniumAdapter(job_id=job.id)
        else:
            scraper = BeautifulSoupAdapter(job_id=job.id)
            
        # Execute Scraper Pipeline
        results = scraper.run(target_url)
        
        # Save results mapping to ScraperResult models
        for res in results:
            ScraperResult.objects.create(
                job=job,
                raw_data=res,
                is_processed=False
            )
            
        job.status = 'COMPLETED'
        job.records_processed = len(results)
        
    except Exception as e:
        logger.error(f"Scraper Job {job_id} failed: {e}")
        if 'job' in locals():
            job.status = 'FAILED'
            job.error_message = str(e)
    finally:
        if 'job' in locals():
            job.completed_at = timezone.now()
            job.save()
