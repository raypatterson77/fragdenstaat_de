from django.utils import timezone

from froide.celery import app as celery_app

from .utils import cleanup_subscribers, send_onboarding_schedule


@celery_app.task(name="fragdenstaat_de.fds_newsletter.cleanup_subscribers")
def cleanup_subscribers_task():
    cleanup_subscribers()


@celery_app.task(name="fragdenstaat_de.fds_newsletter.trigger_onboarding_schedule")
def trigger_onboarding_schedule():
    now = timezone.now()
    today = timezone.localdate(now)
    send_onboarding_schedule(today)
