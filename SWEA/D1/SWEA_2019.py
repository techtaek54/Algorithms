# [SWEA] D1 - 2019. 더블더블

import sys

sys.stdin = open('input_2019.txt', 'r')

num = int(input())

for i in range(num + 1):
  print(2 ** i, end=' ')
