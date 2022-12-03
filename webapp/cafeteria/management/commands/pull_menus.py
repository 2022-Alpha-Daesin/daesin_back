import logging
import requests
from bs4 import BeautifulSoup as bs
from cafeteria.models import Cafeteria,Menu
from django.core.management.base import BaseCommand
logger = logging.getLogger('django')


def classify_cafeteria(date,title):
    if Cafeteria.objects.filter(date=date,name =title).exists():
        cafeteria = Cafeteria.objects.get(date=date,name =title)
    else:
        cafeteria = Cafeteria.objects.create(
            date=date,
            name=title
        )
    return cafeteria

def classify_date(title , date, col,menu):
    if not '운영시간' in menu:
        cafeteria = classify_cafeteria(date, title)
        menu = Menu.objects.create(division = col,food = menu,cafeteria=cafeteria)

def is_recent_updated(date):
    print("시빠",date)
    return Cafeteria.objects.filter(date=date).exists()


class Command(BaseCommand):
    help = 'This is pull_major command'

    def add_argument(self, parser):
        parser.add_argument("--times", help="Command Create")

    def handle(self, *args, **options):
        url = 'https://www.kookmin.ac.kr/user/unLvlh/lvlhSpor/todayMenu/index.do'
        res = requests.get(url)
        soup = bs(res.content, 'html.parser')
        sections = soup.select('.cont_section')
        week_date = sections[0].find_all('th')[2].get_text().replace('.','-').split('(')[0]
        if is_recent_updated(week_date):
                return logger.info('today menus does exist')
        for section in sections:
            title = section.find('p', class_='cont_subtit')
            title_text = title.get_text()
            dates = section.find_all('th')
            bodys = section.find('tbody').find_all('tr')
            for d_index in range(1,len(dates)):
                date_text = dates[d_index].get_text()
                date_text = date_text.replace('.','-').split('(')[0]
                for b_index in range(0,len(bodys)):
                    item = bodys[b_index].find_all('td')[d_index]
                    col = bodys[b_index].find_all('td')[0]
                    if not item.find('input') == []:
                        input_tag = item.find('input')
                        fourvalue = input_tag['value'].replace('{','').replace('}','').split(',')[1].replace(' fourValue=','')
                        if not fourvalue == '':
                            column = col.get_text().replace('\n', '')
                            menu = item.get_text().replace('\n', ' ').replace('\t',' ')
                            classify_date(title_text,date_text,column,menu)
        logger.info('Complete Cafeteria Crawling ')