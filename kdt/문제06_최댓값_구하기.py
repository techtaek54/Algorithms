numbers = list(map(int,input().split()))
max_val = numbers[0]

for i in range(len(numbers)):
  if max_val < numbers[i]:
    max_val = numbers[i]
print(max_val)