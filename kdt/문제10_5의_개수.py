# [KDT1] 파이썬 실습 문제 - 문제 10. 5의 개수 구하기
# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

# input : list
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

# Algorithm
cnt = 0
for number in numbers:
  if number == 5:
    cnt += 1

# output
print(cnt)