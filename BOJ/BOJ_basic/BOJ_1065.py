'''
* 한수 : 각 자리가 등차수열을 이루는 수
* I : 자연수 n (n <= 1000)
* O : 한수의 개수 (<= n)
'''

def hansoo(n):
    cnt = 0
    for i in range(1, n + 1):
        digit_100 = (i // 100) 
        digit_10 = (i % 100 // 10)
        digit_1 = (i % 10)
        if i < 100:
            cnt += 1
        elif (digit_100 - digit_10) == (digit_10 - digit_1):
            cnt += 1
    return cnt

n = int(input())

print(hansoo(n))