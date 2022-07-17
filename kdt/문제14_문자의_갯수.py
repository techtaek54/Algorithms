# [KDT1] 파이썬 실습 문제 - 문제 14. 문자의 갯수 구하기
# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 사용 X

# input : word
word = input()

# Algorithm
cnt = 0
for i in word:
  if i == 'a':
    cnt += 1

# output
print(cnt)