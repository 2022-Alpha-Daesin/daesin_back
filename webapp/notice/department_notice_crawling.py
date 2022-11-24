import re

import requests
from bs4 import BeautifulSoup as bs


def escape_ansi(line):
    ansi_escape = re.compile(r'(\xd7|\n)')
    return ansi_escape.sub('', line).replace('\t', '')


# 유저의 학과 확인 -> 소속 학과의 공지사항 링크 접속 -> 크롤링(제목, 링크 넘겨줌)
def software():
    result = []
    baseUrl = 'https://cs.kookmin.ac.kr/news/notice/'
    res = requests.get(baseUrl)
    soup = bs(res.content, 'html.parser')
    notice = soup.find_all('li', class_='subject')
    for notice_id, n in enumerate(notice):
        notice_title = escape_ansi(n.get_text())
        notice_link = baseUrl + n.find('a', href=True)['href']
        notice_obj = {
            'id': notice_id + 1,
            'major': "소프트웨어학부",
            'title': notice_title,
            'url': notice_link,
        }
        result.append(notice_obj)
    return {'result': result}


def english():
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


def public_administration():
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


def sociology():
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
            'major': "행정학과",
            'title': notice_title,
            'url': notice_link,
        }
        result.append(notice_obj)
    return {"result": result}


def media_advertising():
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


def russian_eurasian():
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


def law():
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


def economics_commerce():
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


def korean():
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


def china():
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
            'major': "한국어문학부",
            'title': notice_title,
            'url': notice_link,
        }
        result.append(notice_obj)
    return {"result": result}


def history():
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


def japan():
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


def mechanical_engineering():
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


def civil_environmental_engineering():
    result = []
    baseUrl = 'https://cee.kookmin.ac.kr/site/board/notice/'
    res = requests.get(baseUrl)
    soup = bs(res.content.decode('euc-kr', 'replace'), 'html.parser')
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


def electronics():
    result = []
    baseUrl = 'https://ee.kookmin.ac.kr/community/board/notice/'
    res = requests.get(baseUrl)
    soup = bs(res.content, 'html.parser')
    notice = soup.find_all('td', class_='subject')
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


print(electronics())
