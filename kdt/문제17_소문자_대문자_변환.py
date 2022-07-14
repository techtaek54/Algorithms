# .upper() 구현
word = input()
for i in range(len(word)):
  c = chr(ord(word[i]) - 32)
  print(c,end='')