'''
* 알람 맞추기
* input : 현재 시간 h1, m1 
* output : 45분 전 시간 h2, m2 (24시간 표현)
'''

h1, m1 = map(int, input().split())

time = (h1 * 60) + m1 - 45

h2 = time // 60 % 24
m2 = time % 60 % 60

print(h2, m2)
