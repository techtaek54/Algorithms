# [KDT1] 파이썬 실습 문제 - 예제 01. 기초 함수
# 숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오. 
# cube 함수를 호출하여 12의 세제곱 결과를 출력하시오

# define function

def cube(n):
  return n ** 3

n = 12
result = cube(n)
print(result)  # 1728