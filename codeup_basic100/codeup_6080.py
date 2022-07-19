# [Codeup 기초 100제] 6080 - 주사위 2개 던지기

n, m = list(map(int, input().split()))

for i in range(1, n + 1):
  for j in range(1, m + 1):
    print(i, j)
