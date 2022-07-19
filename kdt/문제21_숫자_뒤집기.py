# [KDT1] 파이썬 실습 문제 - 문제 21. 숫자 뒤집기
# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# str() 사용 금지

num = int(input())  # 1234 -> 4321
char = 0

while num:
  char = num % 10
  num //= 10
  print(char, end='') 
