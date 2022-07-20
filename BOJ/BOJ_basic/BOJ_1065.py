# str 으로 풀기

num = int(input())

cnt = 0
for i in range(1, num + 1):
    x = str(i)

    if i < 100:
        cnt += 1
    elif (int(x[1]) - int(x[0])) == (int(x[2]) - int(x[1])):
        cnt +=1

print(cnt)

# int 로 풀기

num = int(input())
cnt = 0

for i in range(1, num + 1):
    if i < 100:
        cnt += 1
    elif ((i // 100) - (i % 100 // 10)) == ((i % 100 // 10)) - (i % 10):
        cnt += 1

print(cnt)