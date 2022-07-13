a, d, n = list(map(int,input().split()))

ans = a

for i in range(1,n):
  ans += d
print(ans)