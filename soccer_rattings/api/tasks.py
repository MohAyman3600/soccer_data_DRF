"""Celery tasks."""
from celery import Task
from celery import shared_task
from celery.utils.log import get_task_logger

from ranked.settings import API_URL, API_HEADERS
from api.scraper.model_scrapers import TeamStatsScraper, PlayerStatsScraper

from api.error_handler_mixin import BaseErrorHandlerMixin

logger = get_task_logger(__name__)


class ExtendedTask(BaseErrorHandlerMixin, Task):
    """Extended Task class with error handling."""


@shared_task(base=ExtendedTask)
def fetch_teams_stats():
    """
    Task for fetching teams statistics and saving them.
    """
    teams_scraper = TeamStatsScraper(API_URL, API_HEADERS)
    result = teams_scraper.save_objects()
    return result


@shared_task(base=ExtendedTask)
def fetch_players_stats():
    """
    Task for fetching players statistics and saving them.
    """
    players_scraper = PlayerStatsScraper(API_URL, API_HEADERS)
    result = players_scraper.save_objects()
    return result
