'''
* 구구단
* input : n (단)
* output : 구구단 결과
'''

n = int(input())

for i in range(1, 10):
    print('{} * {} = {}'.format(n, i, n * i))