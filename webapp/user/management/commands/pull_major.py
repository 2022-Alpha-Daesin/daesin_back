import logging

import requests
from bs4 import BeautifulSoup as bs
from django.core.management.base import BaseCommand

from user.models import Major

logger = logging.getLogger('django')
url = 'https://www.kookmin.ac.kr/comm/menu/user/9c61b37c77c0897a4e49f02d7c8cdc78/content/index.do#di1_cont_1'


# 대학 소개 페이지

def select_college_type(college):
    college_tuple = Major.COLLEGE_TYPE
    if college == '글로벌인문·지역대학':
        return college_tuple[0][0]
    for college_element in college_tuple:
        if college_element[1] == college:
            return college_element[0]
    raise Exception


def create_sub_major(db_college, major_title, sub_major):
    if Major.objects.filter(college=db_college).filter(department=major_title, sub_major=sub_major).exists():
        return ''
    Major.objects.create(college=db_college, department=major_title, sub_major=sub_major)
    logger.info(f"{sub_major} : OK")


def create_major(db_college, major_title):
    if Major.objects.filter(college=db_college).filter(department=major_title).exists():
        return ''
    Major.objects.create(college=db_college, department=major_title)
    logger.info(f"{major_title}:OK")


class Command(BaseCommand):
    help = 'This is pull_major command'

    def add_argument(self, parser):
        parser.add_argument("--times", help="Command Create")

    def handle(self, *args, **options):
        response = requests.get(url)
        logger.info(f"응답코드: {response.status_code}")
        html_text = response.text
        html = bs(html_text, 'html.parser')
        for i in range(1, 15):
            college = html.select_one(f'#di1_cont_{i} .cont_tit').get_text()
            db_college = select_college_type(college)
            majors = html.select(f'#di1_cont_{i} .cont_box > div.major_list > div.major_box')
            for major in majors:
                major_title = major.select_one('.major_tit > a > span')
                major_title = major_title.get_text()
                sub_majors = major.select('.sub_major > ul > li')
                create_major(db_college, major_title)
                for sub_major in sub_majors:
                    sub_major = sub_major.get_text()
                    create_sub_major(db_college, major_title, sub_major)
