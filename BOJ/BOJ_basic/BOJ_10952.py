'''
* I : 두 정수 a, b
* O : a + b
* 입력의 마지막에는 0 두 개가 들어옴
'''

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)