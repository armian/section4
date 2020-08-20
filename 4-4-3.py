import urllib.request as req
import simplejson as json
import os.path

# url

url = "https://api.github.com/repositories"

# 경로 & 파일명
savename = "/Users/armian/Inflearn/workspace/section4/repo.json"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

items = json.load(open(savename, 'r', encoding="utf-8"))           # 파일로 부터 바로 역직렬화
#items = json.loads(open(savename, 'r', encoding="utf-8").read())  # 파일 -> 문자열로부터 역직렬화

#출력
for item in items:
    print(item["full_name"]+ "   -   " + item["owner"]["url"])
