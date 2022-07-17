# [KDT1] 파이썬 실습 문제 - 문제 16. 모음 등장 여부 확인하기
# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# count() 사용 X

# input
word = input()

# Algorithm
cnt = 0
for char in word:
  if char in 'aeiou':
    cnt += 1

# output
print(cnt)