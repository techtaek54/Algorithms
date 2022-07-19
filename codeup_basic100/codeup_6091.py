# [Codeup 기초 100제] 6091 - 함께 문제 푸는 날

a, b, c = list(map(int, input().split()))

i = 1
while True:
  if i % a == 0 and i % b == 0 and i % c == 0:
    print(i)
    break
  i += 1
