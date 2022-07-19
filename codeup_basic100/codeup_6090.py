# [Codeup 기초 100제] 6090 - 수 나열하기3

a, m, d, n = list(map(int, input().split()))

for i in range(n - 1):
  a = (a * m) + d

print(a)
