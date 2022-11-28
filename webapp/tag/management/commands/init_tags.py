import logging
from django.core.management.base import BaseCommand
from tag.models import Tag

logger = logging.getLogger('django')

review_categories = [
    '전과/복전/부전','전과','복전','부전','졸업정보','교환학생','장학정보','지원금'
]
ad_categories =[
    '알파프로젝트','알바','기타'
]

class Command(BaseCommand):
    help = 'This is pull_major command'

    def add_argument(self, parser):
        parser.add_argument("--times", help="Command Create")

    def handle(self, *args, **options):
        if Tag.objects.filter(content='후기').exists():
            review = Tag.objects.get(content='후기')
        else:
            review = Tag.objects.create(content ='후기')

        if Tag.objects.filter(content='동아리').exists():
            club = Tag.objects.get(content ='동아리')
        else:
            club = Tag.objects.create(content ='동아리')
        
        if Tag.objects.filter(content='홍보').exists():
            ad = Tag.objects.get(content ='홍보')
        else:
            ad = Tag.objects.create(content ='홍보')
        for category in review_categories:
            if not Tag.objects.filter(content =category).exists():
                Tag.objects.create(content =category,parent=review)
        for category in ad_categories:
            if not Tag.objects.filter(content =category).exists():
                Tag.objects.create(content =category,parent=ad)
        logger.info("tag initialize complete")