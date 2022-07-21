'''
* input : test case T / 두 정수 a, b
* output : a + b
'''

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(a + b)