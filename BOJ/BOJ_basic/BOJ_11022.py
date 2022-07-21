'''
* I : test case T / 두 정수 a, b
* O : a + b
'''

T = int(input())

for i in range(1, T + 1):
    a, b = map(int, input().split())

    print('Case #{}: {} + {} = {}'.format(i, a, b, a + b))