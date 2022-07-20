import sys

t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    ans = a + b
    
    print(ans)