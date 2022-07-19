# [Codeup 기초 100제] 6094 - 이상한 출석 번호 부르기3

n = int(input())
case = list(map(int, input().split()))
min_val = case[0]

# min(case)
for i in range(len(case)):
  if min_val > case[i]:
    min_val = case[i]

print(min_val)
