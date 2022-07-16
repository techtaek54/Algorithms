# [KDT1] 파이썬 실습 문제 - 문제 13. 문자열 조작하기
# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

# input : str
word = input()

# Algorithm
for i in range(len(word)):
  print(word[len(word)-1-i], end='')