# [Codeup 기초 100제] 6077 - 짝수 합 구하기

num = int(input())
sum_val = 0

for i in range(1, num + 1):
  if i % 2 == 0:
    sum_val += i

print(sum_val)