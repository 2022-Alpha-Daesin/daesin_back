import itertools
import re

import requests
from bs4 import BeautifulSoup as bs
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from notice.models import Notice
from notice.serializers import NoticeSerializer
from user.models import UserMajor


class NoticeListAPIView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def list(self, request, *args, **kwargs):
        try:
            user_major = UserMajor.objects.filter(user=self.request.user)
            ret = {}
            for department in user_major:
                data = []
                major_num = department.number
                major = department.major.department
                method_name = eval('self.' + major_dict[major] + '()')
                data.append(method_name)
                data = list(itertools.chain(*data))
                ret[str(major_num)] = data
            return Response(ret, status=status.HTTP_200_OK)
        except TypeError:
            return Response(self.no_login_or_no_major())

    # 비로그인 및 전공이 없는경우 국민대 학사 공지 크롤링
    def no_login_or_no_major(self):
        result = []
        baseUrl = 'https://www.kookmin.ac.kr/user/kmuNews/notice/4/index.do'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('li', class_='notice')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = "https://www.kookmin.ac.kr" + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "국민대학교",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {"1": result}

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
        return result

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
        return result

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
        return result

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
        return result

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
        return result

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
        return result

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
        return result

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
        return result

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
        return result

    # 미디어 광고학부
    def media(self):
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
        return result

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
        return result

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
        return result

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
        return result

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
        return result

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
        return result

    # 건설시스템공학부
    def civil_environmental_engineering(self):
        result = []
        baseUrl = 'https://cee.kookmin.ac.kr/site/board/notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content.decode('euc-kr', 'replace'), 'html.parser')
        notice = soup.find_all('td', class_='subject')[:5]
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
        return result

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
        return result

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
        return result

    # 임산생명공학과
    def bio_tech(self):
        result = []
        baseUrl = 'https://cst.kookmin.ac.kr/community/notice/?sc=220'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find('tbody', class_=False).find_all('tr', class_=False)[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('td', class_='subject title').find('a').get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "임산생명공학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return result

    # 과학기술대학(산림환경시스템학과, 나노전자물리학과, 응용화학과)
    def science_tech(self):
        result = []
        baseUrl = 'https://cst.kookmin.ac.kr/community/notice/?sc=221'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('td', class_='subject title')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "과학기술대학",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return result

    # 정보보안암호수학과
    def security_mathematics(self):
        result = []
        baseUrl = 'https://cst.kookmin.ac.kr/community/notice/?sc=223'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find('tbody', class_=False).find_all('tr', class_=False)[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('td', class_='subject title').find('a').get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "정보보안암호수학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return result

    # 바이오발효융합학과
    def bio_fusion(self):
        result = []
        baseUrl = 'https://cst.kookmin.ac.kr/community/notice/?sc=225'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find('tbody', class_=False).find_all('tr', class_=False)[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('td', class_='subject title').find('a').get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "바이오발융합학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return result

    # 미래모빌리티학과
    def future_mobility(self):
        result = []
        baseUrl = 'https://futuremobility.kookmin.ac.kr/futuremobility/board/academic-news001.do'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('div', class_='b-title-box')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a').get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "미래모빌리티학과",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return result

    # 자동차융합대학 (자동차공학과, 자동차IT융합학과, 미래자동차전공[연계전공])
    def car_fusion(self):
        result = []
        baseUrl = 'https://auto.kookmin.ac.kr/impartation/notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('td', class_='subject')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a').get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "자동차융합대학",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return result

    # 건축학부
    def architecture(self):
        result = []
        baseUrl = 'https://archi.kookmin.ac.kr/site/community/notice.htm'
        res = requests.get(baseUrl)
        soup = bs(res.content.decode('euc-kr', 'replace'), 'html.parser')
        notice = soup.find_all('td', colspan="3")[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a').get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "건축대학",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return result

    # 경영대학 (경영학부, 기업경영학부, 경영정보학부, KIBS, 재무금용 회계학부, AI 빅데이터융합경영학)
    def business(self):
        result = []
        baseUrl = 'https://biz.kookmin.ac.kr/community/notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        # 동일한 태그속성으로 테이블의 "제목"칼럼이 잡혀있어서 인덱스 수정.
        notice = soup.find_all('li', class_='subject')[1:6]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a').get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "경영대학",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return result

    # 체육대학 (스포츠교육학과, 스포츠산업레저학과, 스포츠건강재활학과)
    def sports(self):
        result = []
        baseUrl = 'https://sport.kookmin.ac.kr/sports/notice/notice01.do'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('div', class_='b-title-box')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.find('a', href=True)['title'])
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "체육대학",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return result

    # 예술대학 (음악학부, 미술학부, 공연예술학부)
    def arts(self):
        result = []
        baseUrl = 'https://art.kookmin.ac.kr/community/notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('li', class_='subject')[1:6]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text()).strip()  # 공백제거
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "예술대학",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return result

    # 신소재공학부
    def materials_science(self):
        result = []
        baseUrl = 'https://engineering.kookmin.ac.kr/board/engineering_notice/'
        res = requests.get(baseUrl)
        soup = bs(res.content, 'html.parser')
        notice = soup.find_all('td', class_='subject')[:5]
        for notice_id, n in enumerate(notice):
            notice_title = escape_ansi(n.get_text())
            notice_link = baseUrl + n.find('a', href=True)['href']
            notice_obj = {
                'id': notice_id + 1,
                'major': "창의공과대학",
                'title': notice_title,
                'url': notice_link,
            }
            result.append(notice_obj)
        return {'result': result}


# 이스케이프 문자 제거
def escape_ansi(line):
    ansi_escape = re.compile(r'(\xd7|\n)')
    return ansi_escape.sub('', line).replace('\t', '')


# 학부와 함수 연결
major_dict = {
    '영어영문학부': 'english',
    '중국학부': 'china',
    '한국어문학부': 'korean',
    '한국역사학과': 'history',
    '일본학과': 'japan',
    '정치외교학과': 'politics',
    '행정학과': 'public_administration',
    '사회학과': 'sociology',
    '미디어ㆍ광고학부': 'media',
    '교육학과': 'education',
    '러시아ㆍ유라시아학과': 'russian_eurasian',
    '법학부': 'law',
    '기업융합법학과': 'law',
    '경제학과': 'economics_commerce',
    '국제통상학과': 'economics_commerce',
    '기계공학부': 'mechanical_engineering',
    '건설시스템공학부': 'civil_environmental_engineering',
    '전자공학부': 'electronics',
    '공업디자인학과': 'industrial_degisn',
    '금속공예학과': 'metal_craft',
    '시각디자인학과': 'design',
    '도자공예학과': 'design',
    '의상디자인학과': 'design',
    '공간디자인학과': 'design',
    '영상디자인학과': 'design',
    '자동차·운송디자인학과': 'design',
    'AI디자인학과': 'design',
    '산림환경시스템학과': 'science_tech',
    '나노전자물리학과': 'science_tech',
    '응용화학부': 'science_tech',
    '임산생명공학과': 'bio_tech',
    '정보보안암호수학과': 'security_mathematics',
    '음악학부': 'arts',
    '마술학부': 'arts',
    '공연예술학부': 'arts',
    '스포츠교육학과': 'sports',
    '스포츠산업레저학과': 'sports',
    '스포츠건강재활학과': 'sports',
    '경영학부': 'business',
    '기업경영학부': 'business',
    '경영정보학부': 'business',
    'KMU International Business School': 'business',
    '재무금융·회계학부': 'business',
    'AI빅데이터융합경영학과': 'business',
    '소프트웨어학부': 'software',
    '인공지능학부': 'software',
    '건축학부': 'architecture',
    '자동차공학부': 'car_fusion',
    '자동차IT융합학과': 'car_fusion',
    '미래자동차학부': 'car_fusion',
    '미래모빌리티학과': 'car_fusion',
    '신소재공학부': 'materials_science',
}
