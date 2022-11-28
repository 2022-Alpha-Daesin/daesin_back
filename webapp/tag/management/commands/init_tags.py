import logging
from django.core.management.base import BaseCommand
from tag.models import Tag

logger = logging.getLogger('django')

review_categories = [
    '전과/복전/부전','전과','복전','부전','졸업정보','교환학생','장학정보','지원금'
]

class Command(BaseCommand):
    help = 'This is pull_major command'

    def add_argument(self, parser):
        parser.add_argument("--times", help="Command Create")

    def handle(self, *args, **options):
        review = Tag.objects.create(content ='후기')
        club = Tag.objects.create(content ='동아리')
        ad = Tag.objects.create(content ='홍보')
        for category in review_categories:
            Tag.objects.create(content =category,parent=review)
        logger.info("tag initialize complete")