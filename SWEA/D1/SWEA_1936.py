# [SWEA] D1 - 1936. 1대1 가위바위보

import sys

sys.stdin = open('input_1936.txt', 'r')

a, b = map(int, input().split())

if a > b or (a == 3 and b == 1): result = 'A'
else: result = 'B'

print(result)

