# [SWEA] D1 - 2025. N줄 덧셈

import sys

sys.stdin = open('input_2025.txt', 'r')

num = int(input())
sum = 0

for i in range(1, num + 1):
  sum += i

print(sum) 
