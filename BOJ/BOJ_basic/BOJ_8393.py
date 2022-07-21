'''
* I : 정수 n
* O : 1~n 까지 합
'''

n = int(input())
ans = 0

for i in range(1, n + 1):
    ans += i

print(ans)
