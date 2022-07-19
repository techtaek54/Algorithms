# [KDT1] 파이썬 실습 문제 - 문제 20. 각 자릿수의 합 구하기
# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

num = int(input())

# Algorithm - str()
num = str(num)
ans = 0
for i in num:
  ans += int(i)
print(ans)

# Algorithm - while loop
ans = 0

while num :
  x = num % 10
  ans += x
  num //= 10

print(ans)