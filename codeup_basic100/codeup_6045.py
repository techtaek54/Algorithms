# [Codeup 기초 100제] 6045 - 정수 3개 입력받아 합과 평균 출력하기

a, b, c = list(map(int, input().split()))

sum_val = a + b + c
avg = sum_val / 3

print('{} {:.2f}'.format(sum_val, avg))
