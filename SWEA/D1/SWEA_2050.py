# [SWEA] D1 - 2050. 알파벳을 숫자로 변환

import sys

sys.stdin = open('input_2050.txt', 'r')

alphabet = input()

for word in alphabet:
  num = ord(word) - 64
  print(num, end=' ') 
