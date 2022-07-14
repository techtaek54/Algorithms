word = input()
target = ['a', 'e', 'i', 'o', 'u']
cnt = 0

for i in range(len(word)):
  if word[i] in target:
    cnt += 1

print(cnt)