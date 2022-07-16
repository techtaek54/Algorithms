# [KDT1] 파이썬 실습 문제 - 문제 06. 최댓값 구하기
# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

# input : str -> list(int)
numbers = list(map(int, input().split()))

# Algorithm
max_val = numbers[0]

for i in range(len(numbers)):
  if max_val < numbers[i]:
    max_val = numbers[i]

# output
print(max_val)