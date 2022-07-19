# [SWEA] D1 - 2070. 큰 놈, 작은 놈, 같은 놈

import sys

sys.stdin = open('input_2070.txt', 'r')

t = int(input())

for i in range(1, t + 1):
  a, b = list(map(int, input().split()))
  if a > b: result = '>'
  elif a < b: result = '<'
  else: result = '='
  print('#{} {}'.format(i, result))
