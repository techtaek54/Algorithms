import sys

sys.stdin = open('input_1284.txt', 'r')

t = int(input())
for i in range(1, t + 1):
    p, q, r, s, w = list(map(int, input().split()))
    price_a = p * w
    
    if w <= r:
        price_b = q
    else:
        price_b = q + ((w - r) * s)
    
    payment = min(price_a, price_b)
    
    print('#{} {}'.format(i, payment))