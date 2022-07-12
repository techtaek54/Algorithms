a, b, c = map(int,input().split())

min = a if a < b else b
min = min if min < c else c

print(min)