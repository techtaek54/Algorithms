# [SWEA] D1 - 2068. 최대수 구하기

import sys

sys.stdin = open('input_2068.txt', 'r')

t = int(input())

for i in range(1, t + 1):
    case = list(map(int, input().split()))
    # max_val = max(case) 가능
    max_val = case[0]
    for j in range(len(case)):
        if max_val < case[j]:
            max_val = case[j]
    print('#{} {}'.format(i, max_val))

# max() 구현
max_val = case[0]
for j in range(len(case)):
    if max_val < case[j]:
        max_val = case[j]
