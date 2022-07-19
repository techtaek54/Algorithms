# [Codeup 기초 100제] 6085 - 그림 파일 저장용량 계산하기

w, h, b = list(map(int, input().split()))
cap = (w * h * b) / 8 / 1024 / 1024

print('{:.2f} MB'.format(cap))