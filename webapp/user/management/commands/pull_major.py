from django.core.management.base import BaseCommand
import requests     
from bs4 import BeautifulSoup as bs      
from user.models import Major

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


class Command(BaseCommand):
    help = 'This is pull_major command'

    def add_argument(self,parser):
        parser.add_argument("--times",help="Command Create")
    
    def handle(self, *args, **options):
        response = requests.get(url)   
        print("응답코드:",response.status_code)
        html_text = response.text
        html = bs(html_text, 'html.parser')
        major_list = []
        for i in range(1,15):
            college_obj = {}
            college = html.select_one(f'#di1_cont_{i} .cont_tit').get_text()
            college_obj['college'] = college
            db_college = select_college_type(college)
            majors = html.select(f'#di1_cont_{i} .cont_box > div.major_list > div.major_box')
            major_obj = {}
            for major in majors:
                major_title = major.select_one('.major_tit > a > span')
                major_title = major_title.get_text()
                sub_majors = major.select('.sub_major > ul > li')
                sub_major_list = []
                for sub_major in sub_majors:
                    sub_major = sub_major.get_text()
                    sub_major_list.append(sub_major)
                    Major.objects.create(college = db_college, department = major_title, sub_major=sub_major)
                Major.objects.create(college = db_college, department = major_title)
                major_obj[major_title] = sub_major_list
            college_obj['major'] = major_obj
            major_list.append(college_obj)
        print('save',major_list)
