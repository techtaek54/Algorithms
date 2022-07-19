# [Codeup 기초 100제] 6081 - 16진수 구구단 출력하기

n = int(input(), 16)

for i in range(1, 16):
  print('%X*%X=%X'%(n, i, n * i))  # format code에서 16진법 표시