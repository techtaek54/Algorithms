n, x = map(int, input().split())
case = list(map(int, input().split()))

min_val = x

for i in case:
    if min_val > i:
        print(i, end=' ')