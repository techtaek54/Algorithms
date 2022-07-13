a, b, c = list(map(int,input().split()))
# 최소공배수 구현
i = 1
while True:
  if i % a == 0 and i % b == 0 and i % c == 0:
    ans = i
    break
  i += 1
print(ans)
