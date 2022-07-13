n = int(input())
check = input().split()
for i in range(n):
  check[i] = int(check[i])

min_num = check[0]

for i in range(n):
  if min_num > check[i]:
    min_num = check[i]
print(min_num)