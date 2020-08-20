import urllib.request as req
import requests
from bs4 import BeautifulSoup
import os.path

# 다운로드 url
url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "/Users/armian/Inflearn/workspace/section4/forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    print('다운로드 확인')

# BeautifulSoup 파싱
xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml, "html.parser")

# 지역확인
# 도시별 최저온도를 순차적으로 출력해보자.
# xml 을 파싱할 때는 (select 보다) find가 훨씬 좋다.

# info = {"서울" : [-1, -5, -3, ..., -4], "부산" : [1, 2, 0, ...] ...}
info = {}
for location in soup.find_all("location"):
    loc = location.find("city").string
    #print(loc)
    weather = location.find_all("tmx")
    #print(weather)
    if not (loc in info):
        info[loc] = []

    for tmx in weather:
        info[loc].append(tmx.string)

#print(info)
#print(sorted(info.keys()))
#print(list(info.keys()))
#print(info.values())

# 각 지역별 날씨 텍스트 쓰기
with open("/Users/armian/Inflearn/workspace/section4/forecast.txt", 'wt') as f:
    for loc in sorted(info.keys()):
        print("+",loc)
        f.write(str(loc)+'\n')
        for n in info[loc]:
            print("-",n)
            f.write('\t'+str(n)+'\n')
