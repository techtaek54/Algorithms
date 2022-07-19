# [Codeup 기초 100제] 6044 - 정수 2개 입력받아 자동 계산하기

a, b = list(map(int, input().split()))

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print('{:.2f}'.format(a / b))