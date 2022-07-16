# [KDT1] 파이썬 실습 문제 - 문제 08. 두번째로 큰 수 구하기
# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

# input : str -> list(int)
# set()을 활용하여 사전에 중복 제거 후 list로 변환
numbers = list(set(map(int, input().split())))

# # Algorithm 1. sort() 구현
for i in range(len(numbers)):
  for j in range(len(numbers)-1-i):
    if numbers[j] > numbers[j+1]:
      numbers[j], numbers[j+1] = numbers[j+1], numbers[j]  # swap by tuple

print(numbers[-2])  # 오름차순에서 뒤에서 두번째 == 두번째로 큰 수


# Algorithm 2. 두 개의 변수를 활용하여 밀어내기
# set() 활용 X
numbers = list(map(int, input().split()))

max_1st = numbers[0]
max_2nd = numbers[0]

for i in range(len(numbers)):
  if max_1st < numbers[i]:
    max_2nd = max_1st
    max_1st = numbers[i]
  elif max_2nd < numbers[i] < max_1st:
    max_2nd = numbers[i]

print(max_2nd)






# # 2. max_2nd로 구하기

# numbers = list(map(int,input().split()))
# max_1st = numbers[0]
# max_2nd = numbers[0]

# for i in range(len(numbers)):
#   if max_1st < numbers[i]:
#     max_2nd = max_1st
#     max_1st = numbers[i]
#   elif max_2nd < numbers[i] < max_1st:
#     max_2nd = numbers[i]
# print(max_2nd)