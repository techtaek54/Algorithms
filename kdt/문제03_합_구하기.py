# [KDT1] 파이썬 실습 문제 - 문제 03. 합 구하기
# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 사용 X

# input : str -> int
n = int(input())

# Algorithm 1. while loop -> sum() 구현
ans = 0
i = 1  # 0 부터 더할 필요 x

while i <= n:
  ans += i
  i += 1


# Algorithm 2. for loop -> sum() 구현
ans = 0

for i in range(1,n+1):  # range()범위 주의
  ans += i

# output : int
print(ans)