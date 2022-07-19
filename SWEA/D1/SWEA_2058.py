# [SWEA] D1 - 2058. 자릿수 더하기

import sys

sys.stdin = open('input_2058.txt', 'r')

n = int(input())
sum = 0

while n:
    x = n % 10
    sum += x
    n //= 10

print(sum)

