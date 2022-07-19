# [SWEA] D1 - 2043. 서랍의 비밀번호

import sys

sys.stdin = open('input_2043.txt', 'r')

p, k = map(int, input().split())

cnt = 0

for i in range(k, p + 1):
  cnt += 1

print(cnt)