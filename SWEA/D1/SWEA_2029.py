# [SWEA] D1 - 2029. 몫과 나머지 출력하기

import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for i in range(1, t + 1):
  a, b = list(map(int, input().split()))
  print('#{} {} {}'.format(i, a // b, a % b))

 