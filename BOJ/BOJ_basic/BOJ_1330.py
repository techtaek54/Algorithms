'''
* input : a, b
* output : 비교연산자 기호
* if-elif-else
'''

a, b = map(int, input().split())

if a > b:
    result = '>'
elif a < b:
    result = '<'
else:
    result = '=='

print(result)