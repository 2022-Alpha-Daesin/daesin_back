import logging

from django.contrib.sites import requests
from django.core.management import BaseCommand

url = "https://www.kookmin.ac.kr/user/unLvlh/lvlhSpor/todayMenu/index.do"
logger = logging.getLogger('django')


class Command(BaseCommand):
    help = 'This is pull_food command'

    def handle(self, *args, **options):
        response = requests.get(url)
        logger.info(f"응답코드: {response.status_code}")
        html_text = response.text
