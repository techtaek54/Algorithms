# [KDT1] 파이썬 실습 문제 - 문제 05. 평균 구하기
# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

# input : str -> list
numbers = list(map(int, input().split()))

# Algorithm
# 1) len() 구현
cnt = 0

for i in numbers:
  cnt += 1

# 2) sum() 구현
ans = 0

for i in range(cnt):
  ans += numbers[i]

# 3) 평균
avg = ans / cnt

# output : float
print(avg)