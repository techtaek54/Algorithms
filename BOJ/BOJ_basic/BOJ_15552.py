'''
* 빠른 연산 : input() -> sys.stdin.readline()
    * 마찬가지로 문자열로 받음, 개행문자까지 같이 받음
* I : test case T / 두 정수 a, b
* O : a + b
'''

import sys

T = int(sys.stdin.readline())

for i in range(1, T + 1):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)