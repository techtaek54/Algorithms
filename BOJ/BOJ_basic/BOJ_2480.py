'''
* 주사위 세개
* input : 주사위 눈 a, b, c
* output : 주어진 조건에 따른 상금
'''

a, b, c = map(int, input().split())

# 같은 눈 3개 
if a == b == c:
    money = 10000 + (a * 1000)
# 같은 눈 2개
elif a == b or a == c:
    money = 1000 + (a * 100)
elif b == c:
    money = 1000 + (b * 100)
# 모두 다른 눈 (나머지 경우)
else:
    money = max(a, b, c) * 100

print(money)

# max() 구현
# max_val = a if a > b else b
# max_val = max_val if max_val > c else c
