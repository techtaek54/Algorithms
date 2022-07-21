'''
- a, b, c 입력받아 다양한 나머지 연산 수행
'''

a, b, c = map(int, input().split())

eq1 = (a + b) % c
eq2 = ((a % c) + (b % c)) % c
eq3 = (a * b) % c
eq4 = ((a % c) * (b % c)) % c

print(eq1)
print(eq2)
print(eq3)
print(eq4)