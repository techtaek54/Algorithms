# [Codeup 기초 100제] 6083 - 빛 섞어 색 만들기

r, g, b = list(map(int, input().split()))
cnt = 0

for i in range(r):
  for j in range(g):
    for k in range(b):
      print(i, j, k)
      cnt += 1
print(cnt)