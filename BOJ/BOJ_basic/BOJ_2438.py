'''
* 별찍기
* I : 계단 수 n
* O : 별계단
'''

n = int(input())

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()
