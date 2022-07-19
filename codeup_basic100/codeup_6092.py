# [Codeup 기초 100제] 6092 - 이상한 출석 번호 부르기1

# input
n = int(input())
called = list(map(int, input().split()))

# result 초기화
result = []
for i in range(23):
  result += [0]

# result의 번호를 체크
for i in range(len(called)):
  result[called[i]-1] += 1

# output
for i in range(len(result)):
  print(result[i],end=' ')