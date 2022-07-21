'''
* 별찍기
* I : 정수 n
* O : 별계단
    * 공백 / 별 / 줄바꿈
'''

n = int(input())

for i in range(n):
    for j in range(n - 1 - i):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()