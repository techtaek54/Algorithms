# [Codeup 기초 100제] 6084 - 소리 파일 저장용량 계산하기

h, b, c, s = list(map(int, input().split()))
cap = (h * b * c * s) / 8 / 1024 / 1024

print('{:.1f} MB'.format(cap))
