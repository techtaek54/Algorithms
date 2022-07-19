# [Codeup 기초 100제] 6043 - 실수 2개 입력받아 나눈 결과 계산하기

f1, f2 = list(map(float, input().split()))

print('{:.3f}'.format(f1 / f2))