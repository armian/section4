# 딕셔너리 자료형(key, value) -> (순서 X, 중복 X, 수정 O, 삭제 O)

# 선언
a = {'name':'kim', 'phone':'0107777777','birth':910809}
b = {0:'Hello World!'}
c = {'arr':[0,1,2,3]}

print(type(a),a)

# 출력
print('a - ', a['name'])
print('a - ', a.get('name'))

# 2가지 방법이 있으나, get()은 없는 경우에 None을 반환
#print('a -', a['address'])
print('a -', a.get('address'))

print('c -', type(c.get('arr')))

# 딕셔너리 추가
a['address'] = 'Seoul'
print('a - ', a)
a['rnak'] = [1, 2, 3]
print('a - ', a)

print('a - ', a.keys())
print('a - ', list(a.keys()))

print('a - ', a.values())
print('a - ', list(a.values()))

print('a - ', a.items())  # tuple로 반환
print('a - ', list(a.items())[1]) # type은 여전히 tuple

print('a - ', 'name' in a)
print('a - ', 'city' in a)
