'''
* x 보다 작은 수
* I : 정수 n, x / list a (n)
* O : x 보다 작은 수 순서대로
'''

n, x = map(int, input().split())
array_n = list(map(int, input().split()))

for i in range(len(array_n)):
    if array_n[i] < x:
        print(array_n[i], end=' ')