# [KDT1] 파이썬 실습 문제 - 문제 07. 최솟값 구하기
# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

# input : str -> list
numbers = list(map(int, input().split()))

# Algorithm
min_val = numbers[0]

for i in range(len(numbers)):
  if min_val > numbers[i]:
    min_val = numbers[i]

# output
print(min_val)
