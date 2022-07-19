# [Codeup 기초 100제] 6063 - 정수 2개 입력받아 큰 값 출력하기

a, b = list(map(int, input().split()))

max_val = a if a > b else b

print(max_val)

