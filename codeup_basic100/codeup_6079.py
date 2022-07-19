# [Codeup 기초 100제] 6079 - 언제까지 더해야 할까?

num = int(input())
sum = 0
i = 0
while True:
  i += 1
  sum += i
  if sum >= num:
    print(i)
    break
