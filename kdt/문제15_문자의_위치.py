# index() find() 구현
word = input()
for i in range(len(word)):
  if word[i] == 'a':
    break
else:
  i = -1
  # if i == len(word)-1:
  #   i = -1
  #   break
print(i)