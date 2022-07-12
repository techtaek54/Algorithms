n = int(input())

# for문
sum = 0
for i in range(1,n+1):
  sum += i
print(sum)

# while문
i = 0
sum = 0

while i <= n:
  sum += i
  i += 1
print(sum)