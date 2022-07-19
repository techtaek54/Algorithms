# [Codeup 기초 100제] 6070 - 월 입력받아 계절 출력하기

month = int(input())

if month // 3 == 1: season = 'spring'
elif month // 3 == 2: season = 'summer'
elif month // 3 == 3: season = 'fall'
else: season = 'winter'

print(season)
