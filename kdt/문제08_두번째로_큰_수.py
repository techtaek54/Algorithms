# 1. set() & sort() 활용 및 구현
# set() 활용하여 중복 제거
numbers = list(set(map(int,input().split())))

# sort()를 구현하여 indexing으로 접근
for i in range(len(numbers)-1):
  for j in range(len(numbers)-1-i):
    if numbers[j] > numbers[j+1]:
      numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers[-2])

# 2. max_2nd로 구하기

numbers = list(map(int,input().split()))
max_1st = numbers[0]
max_2nd = numbers[0]

for i in range(len(numbers)):
  if max_1st < numbers[i]:
    max_2nd = max_1st
    max_1st = numbers[i]
  elif max_2nd < numbers[i] < max_1st:
    max_2nd = numbers[i]
print(max_2nd)