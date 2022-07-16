# [KDT1] 파이썬 실습 문제 - 문제 02. 길이 구하기
# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.
# len() 사용 X

# input : str
word = input()

# Algorithm : len() 구현
cnt = 0

for i in word:
  cnt += 1

# output : int
print(cnt)
