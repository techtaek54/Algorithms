x = int(input())
check = input().split()

for i in range(x):
  check[i] = int(check[i])

# 1~23번까지, 0은 사용 X
student = []
for _ in range(24):
  student.append(0)

for i in range(x):
  student[check[i]] += 1

for i in range(1,24):
  print(student[i],end=' ')
