students = list(map(int, input().split()))
cnt = 0

for i in range(len(students)):
  if students[i] == '이영희':
    cnt += 1

print(cnt)