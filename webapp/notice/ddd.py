import re

import requests
from bs4 import BeautifulSoup as bs


# 이스케이프 문자 제거
def escape_ansi(line):
    ansi_escape = re.compile(r'(\xd7|\n)')
    return ansi_escape.sub('', line).replace('\t', '')


def sports():
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
    return {"result": result}


print(sports())
