h, b, c, s = list(map(int,input().split()))

cap = (h * b * c * s) / 8 / 1024 / 1024
print('{:.1f} MB'.format(cap))