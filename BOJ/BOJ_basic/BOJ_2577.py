'''
* 숫자의 개수
* I : a, b, c 한 줄씩 (100 <= a,b,c < 1000 = > 3자리)
* O : a * b * c 에 0~9 가 얼마씩 있는지 한 줄씩 출력 
'''

a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)
result = []

# count() 사용
for i in range(10):
    result.append(mul.count(str(i)))

for i in range(10):
    print(result[i])

# count() 직접 구현

for i in range(10):
    cnt = 0
    for j in range(len(mul)):
        if str(i) == mul[j]:
            cnt += 1
    print(cnt)
