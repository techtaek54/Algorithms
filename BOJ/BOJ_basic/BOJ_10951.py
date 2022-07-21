'''
* I : 두 정수 a, b
* O : a + b
* try-except 처리
'''

while True:
    try:
        a, b = map(int, input().split())
    except:
        break    
    print(a + b)