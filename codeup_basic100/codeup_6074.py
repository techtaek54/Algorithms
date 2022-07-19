# [Codeup 기초 100제] 6074 - 문자 1개 입력받아 알파벳 출력하기

c = ord(input())

for i in range(ord('a'),c+1):
  print(chr(i), end=' ')
