w, h, b = list(map(int,input().split()))
cap = (w * h * b) / 8 / 1024 / 1024
print(f'{cap:.2f} MB')