# [Codeup 기초 100제] 6089 - 수 나열하기2

a, r, n = list(map(int, input().split()))

for i in range(n-1):
  a *= r

print(a)