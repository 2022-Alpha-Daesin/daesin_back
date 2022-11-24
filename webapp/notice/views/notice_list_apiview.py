import re

import requests
from bs4 import BeautifulSoup as bs
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from notice.models import Notice
from notice.serializers import NoticeSerializer


class NoticeListAPIView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def list(self, request, *args, **kwargs):
        return Response(self.public_administration())

    # 소프트웨어융합대학(소프트웨어학부, 인공지능학부)
    def software(self):
        result = []
        baseUrl = 'https://cs.kookmin.ac.kr/news/notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('li', class_='subject')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "소프트웨어융합대학",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 영어영문학부
    def english(self):
        result = []
        baseUrl = 'https://cha.kookmin.ac.kr/english/english_notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('td', class_='subject title')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "영어영문학부",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 중국학부
    def china(self):
        result = []
        baseUrl = 'https://cha.kookmin.ac.kr/china/china_notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('td', class_='subject title')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "중국학부",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 한국어문학부
    def korean(self):
        result = []
        baseUrl = 'https://cha.kookmin.ac.kr/korea/korea_notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('td', class_='subject title')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text()).replace("\xa0", "")
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "한국어문학부",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 한국역사학과
    def history(self):
        result = []
        baseUrl = 'https://cha.kookmin.ac.kr/history/history_notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('td', class_='subject title')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "한국역사학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 일본학과
    def japan(self):
        result = []
        baseUrl = 'https://cha.kookmin.ac.kr/japan/japan_notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('td', class_='subject title')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "일본학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 정치외교학과
    def politics(self):
        result = []
        baseUrl = 'https://polisci.kookmin.ac.kr/polisci/etc-board/board02.do'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('div', class_='b-title-box')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a', href=True)['title'])
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "정치외교학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 행정학과
    def public_administration(self):
        result = []
        baseUrl = 'https://paap.kookmin.ac.kr/paap/notice/notice.do'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('div', class_='b-title-box')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a', href=True)['title'])
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "행정학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 사회학과
    def sociology(self):
        result = []
        baseUrl = 'https://kmusoc.kookmin.ac.kr/kmusoc/etc-board/major_notice.do'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('div', class_='b-title-box')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a', href=True)['title'])
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "사회학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 미디어 광고학부
    def media_advertising(self):
        result = []
        baseUrl = 'https://cms.kookmin.ac.kr/kmumedia/community/major-notice.do'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('div', class_='b-title-box')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a', href=True)['title']).replace(" 자세히 보기", '')
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "미디어광고학부",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 교육학과
    def education(self):
        result = []
        baseUrl = 'https://cms.kookmin.ac.kr/kmuedu/community/notice.do'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('div', class_='b-title-box')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a', href=True)['title']).replace(" 자세히 보기", '')
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "교육학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 러시아 유라시아 학과
    def russian_eurasian(self):
        result = []
        baseUrl = 'https://cms.kookmin.ac.kr/Russian-EurasianStudies/community/department-notice.do'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('div', class_='b-title-box')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a', href=True)['title']).replace(" 자세히 보기", '')
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "러시아_유라시아학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 법과대학(법학부, 기업융합법학과)
    def law(self):
        result = []
        baseUrl = 'https://law.kookmin.ac.kr/bachelor/notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('td', class_='title')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "법학부",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 경상대학(경제학과, 국제통상학과)
    def economics_commerce(self):
        result = []
        baseUrl = 'https://kyungsang.kookmin.ac.kr/community/board/notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('li', class_='subject')[1:6]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "경상대학",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 기계공학부
    def mechanical_engineering(self):
        result = []
        baseUrl = 'https://me.kookmin.ac.kr/mech/bbs/notice.do'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('div', class_='b-title-box')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a', href=True)['title']).replace(' 자세히 보기', '')
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "기계공학부",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 건설시스템공학부
    def civil_environmental_engineering(self):
        result = []
        baseUrl = 'https://cee.kookmin.ac.kr/site/board/notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content.decode('euc-kr', 'replace'), 'html.parser')[:5]
        notice = soup.find_all('td', class_='subject')
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text()).replace('\r', '')
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "건설시스템공학부",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {'result': result}

    # 전자공학부
    def electronics(self):
        result = []
        baseUrl = 'https://ee.kookmin.ac.kr/community/board/notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('td', class_='subject')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "전자공학부",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {'result': result}

    # 공업디자인학과
    def industrial_degisn(self):
        result = []
        baseUrl = 'https://id.kookmin.ac.kr/id/intro/notice.do'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('div', class_='b-title-box')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a', href=True)['title'])
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "공업디자인학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 금속공예학과
    def metal_craft(self):
        result = []
        baseUrl = 'http://mcraft.kookmin.ac.kr/?page_id=516'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('div', class_='cut_strings')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "금속공예학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}

    # 조형대학(시각디자인학과, 도자공예학과, 의상디자인학과, 공간디자인학과, 영상디자인학과, 자동차운송디자인학과, AI디자인학과)
    def design(self):
        result = []
        baseUrl = 'https://design.kookmin.ac.kr/community/notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find('ul', class_='article-list bar-type').find_all('li', class_=False)
        for notice_id, n in enumerate(notice):
            notice_title = n.find('a').find('strong').get_text()
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "조형대학",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"result": result}


# 이스케이프 문자 제거
def escape_ansi(line):
    ansi_escape = re.compile(r'(\xd7|\n)')
    return ansi_escape.sub('', line).replace('\t', '')
