# [SWEA] D1 - 1933. 간단한 N의 약수

import sys

sys.stdin = open('input_1933.txt', 'r')

num = int(input())

for i in range(1, num + 1):
  if num % i == 0:
    print(i, end=' ')