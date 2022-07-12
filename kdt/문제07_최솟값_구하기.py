numbers = list(map(int,input().split()))
min_val = numbers[0]

for i in range(len(numbers)):
  if min_val > numbers[i]:
    min_val = numbers[i]
print(min_val)