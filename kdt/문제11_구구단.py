# [KDT1] 파이썬 실습 문제 - 문제 11. 구구단 출력하기
# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

# Algorithm
for i in range(2,10):
  print('{}단'.format(i))
  for j in range(1,10):
    print('{} X {} = {}'.format(i, j, i * j))