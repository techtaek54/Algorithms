a, b = map(int, input().split())  # 현재 시각
c = int(input())  # 소요시간

total_time = (a * 60 + b) + c
hour = total_time // 60 % 24
min = total_time % 60 % 60

print(hour, min)