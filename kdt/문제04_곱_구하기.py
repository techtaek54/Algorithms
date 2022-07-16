# [KDT1] 파이썬 실습 문제 - 문제 04. 곱 구하기
# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# input : str -> int
n = int(input())

# Algorithm 1. while loop
i = 1
ans = 1

while i <= n:
  ans *= i
  i += 1

# Algorithm 2. for loop
ans = 1

for i in range(1,n+1):
  ans *= i

# output : int
print(ans)