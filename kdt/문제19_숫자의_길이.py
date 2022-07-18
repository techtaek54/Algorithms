# [KDT1] 파이썬 실습 문제 - 문제 19. 숫자의 길이 구하기
# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

number = 123  # output : 3
i = 0
while True:
  if not number // (10 ** i):
    break
  i += 1

print(i)

