'''
- 3 6 9가 들어 있는 경우 `박수(-)` 표시
- 36 => `__` / 369 => `--` 로 표시 
'''
import sys

sys.stdin = open('input_1926.txt', 'r')

n = int(input())

for i in range(1, n + 1):
    num = str(i)
    if '3' in num or '6' in num or '9' in num:
        digit_3 = num.count('3')
        digit_6 = num.count('6')
        digit_9 = num.count('9')
        digit_sum = digit_3 + digit_6 + digit_9
        i = '-' * digit_sum

    print(i, end=' ')


            
