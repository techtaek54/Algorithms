# [SWEA] D1 - 2072. 최대수 구하기

import sys

sys.stdin = open('input_2072.txt', 'r')

t = int(input())

for i in range(1, t + 1):
    case = list(map(int, input().split()))
    sum = 0
    for j in range(len(case)):
        if case[j] % 2 == 1:
            sum += case[j]
    print('#{} {}'.format(i, sum))