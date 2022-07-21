'''
- 시, 분 => 더한 값 => 시, 분 출력 (12시간제 => %12)

'''
import sys

sys.stdin = open('input_1976.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    hour, minute, plus_hour, plus_minute = map(int, input().split())

    total_time = (hour * 60 + minute) + (plus_hour * 60 + plus_minute)
    total_hour = total_time // 60 % 12
    if total_hour == 0:
        total_hour = 12
    total_minute = total_time % 60 % 60
    
    print('#{} {} {}'.format(i, total_hour, total_minute)) 