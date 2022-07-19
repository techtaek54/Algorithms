# [SWEA] D1 - 2071. 평균값 구하기

import sys

sys.stdin = open('input_2071.txt', 'r')

t = int(input())

for i in range(1, t + 1):
  a = list(map(int, input().split()))
  avg = sum(a) / len(a)

  print('#{} {}'.format(i, round(avg)))
