# [Codeup 기초 100제] 6093 - 이상한 출석 번호 부르기2

n = int(input())
case = list(map(int, input().split()))

for i in range(len(case)):
    print(case[len(case)-1-i], end=' ')
