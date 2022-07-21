'''
* 오븐 시계
* input : 현재 시간 h1, m1 / 필요한 시간 plus_time
* output : 나중 시간 h2, m2 (24시간 표현)
'''

h1, m1 = map(int, input().split())
plus_time = int(input())

time = (h1 * 60) + m1 + plus_time

h2 = time // 60 % 24
m2 = time % 60 % 60

print(h2, m2)

