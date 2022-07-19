# input : 24시간 표현 사용 => 0:0 ~23:59 
# 45분 이른 시간 출력
h, m = map(int, input().split())

set_time = (h * 60 + m) - 45
hour = set_time // 60 % 24
min = set_time % 60 % 60

print(hour, min)




