# sum(), len() 사용 X

numbers = list(map(int,input().split()))
sum = 0
cnt = 0

for i in numbers:
  sum += i
  cnt += 1

avg = sum / cnt
print(avg)