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
    def sof(self):
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

    # 글로인문지역대학 (한국어문학부, 영어영문학부, 중국학부, 한국역사학과)
    def lib(self):
        result = []
        baseUrl = 'https://cha.kookmin.ac.kr/community/college/notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('td', class_='subject title')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "글로벌인문지역대학",
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


# 이스케이프 문자 제거
def escape_ansi(line):
    ansi_escape = re.compile(r'(\xd7|\n)')
    return ansi_escape.sub('', line).replace('\t', '')
