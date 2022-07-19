# [SWEA] D1 - 2063. 중간값 찾기

import sys

sys.stdin = open('input_2063.txt', 'r')

n = int(input())
ans = list(map(int, input().split()))
ans.sort()  # 오름차순 정렬
i = n  // 2

print(ans[i])
