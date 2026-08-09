from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from apps.universities.models import University
from apps.scraping.models import ScraperJob
import json

@receiver(post_save, sender=University)
def notify_new_university(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'global_notifications',
            {
                'type': 'send_notification',
                'message': f'New university added: {instance.canonical_name}',
                'event_type': 'university_created'
            }
        )

@receiver(post_save, sender=ScraperJob)
def notify_scraper_job_status(sender, instance, **kwargs):
    # Notify on scraper job updates
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'global_notifications',
        {
            'type': 'send_notification',
            'message': f'Scraper Job {instance.id} status updated to {instance.status}',
            'event_type': 'scraper_status'
        }
    )

from apps.professors.models import Professor
from apps.scholarships.models import Scholarship

@receiver(post_save, sender=Professor)
def notify_new_professor(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'global_notifications',
            {
                'type': 'send_notification',
                'message': f'New professor scraped: {instance.name} from {instance.university.canonical_name}',
                'event_type': 'professor_created'
            }
        )

@receiver(post_save, sender=Scholarship)
def notify_new_scholarship(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        opening = instance.opening_date.strftime('%b %d, %Y') if instance.opening_date else 'Not Specified'
        deadline = instance.deadline.strftime('%b %d, %Y') if instance.deadline else 'Not Specified'
        news = f"Special: {instance.funding_type}" if instance.funding_type else "New Opportunity!"
        
        async_to_sync(channel_layer.group_send)(
            'global_notifications',
            {
                'type': 'send_notification',
                'message': f'New Scholarship Found: {instance.name} | Release: {opening} | Expires: {deadline} | {news}',
                'event_type': 'scholarship_created'
            }
        )

