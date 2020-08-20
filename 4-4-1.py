import simplejson as json
#import json

# Dict(Json) 선언

data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Seoul'
})

data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Busan'
})

data['people'].append({
    'name':'Lee',
    'website':'daum.net',
    'from':'Incheon'
})

#print(data)
"""
{
    "people": [
        {
            "name": "Kim",
            "website": "naver.com",
            "from": "Seoul"
        },
        {
            "name": "Park",
            "website": "google.com",
            "from": "Busan"
        },
        {
            "name": "Lee",
            "website": "daum.net",
            "from": "Incheon"
        }
    ]
}
"""

# Dict(Json) -> Str

#e = json.dumps(data)  # 파일로 저장가능하다 (문자열이기 때문에))
e = json.dumps(data, indent=4)  # 이렇게 저장하면 보기 좋네^^
print(type(e))
print(e)

# Str -> Dict(Json)
d = json.loads(e)
print(type(d))
print(d)

with open("/Users/armian/Inflearn/workspace/section4/member.json", 'w') as outfile:
    outfile.write(e)

# https://jsoneditoronline.org 에서 변환해서 보면 좋음

with open("/Users/armian/Inflearn/workspace/section4/member.json", 'r') as infile:
    r = json.loads(infile.read())
    print("=====")
    print(type(r))
    print(r)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
