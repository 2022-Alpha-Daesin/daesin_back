import re

import requests
from bs4 import BeautifulSoup as bs

# 한울식당
url = "https://kmucoop.kookmin.ac.kr/restaurant/restaurant.php?mkey=3&w=1"

response = requests.get(url, verify=False)
html = bs(response.content.decode('euc-kr,', 'replace'), 'html.parser')
text = html.select('table.ft1')[1]
date = text.find_all('span')[:7]

# 날짜 크롤링
for i in date:
    print(i.get_text())

# 식당 이름 크롤링
for i in text.select('td.mn_corn')[2:6]:
    print(re.sub('[0-9]코너', '', i.get_text()))

# 메뉴 크롤링
for i in text.select('td.ft1')[14:]:
    print('&&&&&&&&&&&&&&')
    print(i.get_text())
