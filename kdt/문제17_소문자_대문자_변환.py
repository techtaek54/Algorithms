# [KDT1] 파이썬 실습 문제 - 문제 17. 소문자-대문자 변환하기
# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper() / .swapcase() 사용 X

# input
word = input()

# Alogorithm
for char in word:
  print(chr(ord(char)-32),end='')