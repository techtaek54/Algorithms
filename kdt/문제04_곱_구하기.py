n = int(input())

# for문
ans = 1

for i in range(1,n+1):
  ans *= i
print(ans)

# while문
ans = 1
i = 1

while i <= n:
  ans *= i
  i += 1
print(ans)