# [SWEA] D1 - 2056. 연월일 달력

import sys

sys.stdin = open('input_2056.txt', 'r')

t = int(input())

for i in range(1, t + 1):
  y = input()
  year = y[:4]
  month = y[4:6]
  day = y[6:]
  if (month in ['01', '03', '05', '07', '08', '10', '12']) and (int(y[6:]) <= 31):
    print('#{} {}/{}/{}'.format(i, year, month, day))
  elif (month in ['04', '06', '09', '11']) and (int(day) <= 30):
    print('#{} {}/{}/{}'.format(i, year, month, day))
  elif (month in ['02']) and (int(day) <= 28):
    print('#{} {}/{}/{}'.format(i, year, month, day))
  else:
    print('#{} -1'.format(i))