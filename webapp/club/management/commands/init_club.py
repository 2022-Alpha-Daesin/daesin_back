import logging

from django.core.management.base import BaseCommand
from ..club_data import clubs 
from club.models import Club

logger = logging.getLogger('django')




class Command(BaseCommand):
    help = 'This is pull_major command'

    def add_argument(self, parser):
        parser.add_argument("--times", help="Command Create")

    def handle(self, *args, **options):
        for club in clubs:
           if not Club.objects.filter(place=club['place']).exists():
                Club.objects.create(**club)
        logger.info("club initialize complete")
