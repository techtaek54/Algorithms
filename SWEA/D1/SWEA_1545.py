# [SWEA] D1 - 1545. 거꾸로 출력해보아요

import sys

sys.stdin = open('SampleInput.txt', 'r')

t = int(input())
for i in range(t + 1):
  print(t - i, end=' ')
