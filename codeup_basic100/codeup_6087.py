# [Codeup 기초 100제] 6087 - 3의 배수는 통과

num = int(input())

for i in range(1, num + 1):
  if i % 3 == 0:
    continue
  print(i, end=' ')
