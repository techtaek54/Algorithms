# [Codeup 기초 100제] 6064 - 정수 3개 입력받아 가장 작은 값 출력하기

a, b, c = list(map(int, input().split()))
min_val = b if b < a else a
min_val = c if c < min_val else min_val

print(min_val)