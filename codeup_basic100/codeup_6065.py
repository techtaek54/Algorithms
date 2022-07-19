# [Codeup 기초 100제] 6065 - 정수 3개 입력받아 짝수만 출력하기

a = list(map(int, input().split()))

for i in range(len(a)):
  if a[i] % 2 == 0:
    print(a[i])
