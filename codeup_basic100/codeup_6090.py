a, m, d, n = list(map(int,input().split()))
ans = a
for i in range(0,n-1):
  ans = (ans * m) + d
print(ans)