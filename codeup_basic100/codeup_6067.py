# [Codeup 기초 100제] 6067 - 정수 1개 입력받아 분류하기

num = int(input())

if num < 0 and num % 2 == 0: result = 'A'
elif num < 0 and num % 2 == 1: result = 'B'
elif num > 0 and num % 2 == 0: result = 'C'
else: result = 'D'

print(result)