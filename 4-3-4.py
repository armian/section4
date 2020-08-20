# Set 집합자료형 (순서 X, 중복 X)

a = set()
b = set([1, 2, 3, 4])

print(type(b))
print(b)

# set은 인덱싱이 안되므로, 아래외 같이 튜플이나 리스트로 변환하여 사용해야 함
t = tuple(b)
print(type(t),t)
print(t[0:2])

l = list(b)
print(type(l),l)
print(l[0:2])

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print('t - ', s1 & s2)
print('t - ', s1.intersection(s2))

print('t - ', s1 | s2)
print('t - ', s1.union(s2))

print('t - ', s1 - s2)
print('t - ', s1.difference(s2))

# 추가, 제거
s3 = set([0,1,2,3])
s3.add(4)
print('s3 - ', s3)

s3.remove(2)
print('s3 - ', s3)
