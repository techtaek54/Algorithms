# [Codeup 기초 100제] 6086 - 거기까지! 이제 그만~

a = int(input())
i = 0
sum = 0

while True:
  i += 1
  sum += i
  if sum >= a:
    print(sum)
    break