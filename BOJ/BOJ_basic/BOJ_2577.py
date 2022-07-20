a = int(input())
b = int(input())
c = int(input())

mul_val = str(a * b * c)  # 0의 개수 카운트 위해 casting

for i in range(10):
    cnt = mul_val.count(str(i))
    print(cnt)

# count() 직접 구현
for i in range(10):
    cnt = 0
    for j in mul_val:
        if str(i) == j:
            cnt +=1
    print(cnt)
