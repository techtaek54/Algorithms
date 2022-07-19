# [Codeup 기초 100제] 6088 - 수 나열하기1

a, d, n = list(map(int, input().split()))

for i in range(n-1):
  a += d

print(a)
