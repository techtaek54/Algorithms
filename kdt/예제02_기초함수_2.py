# [KDT1] 파이썬 실습 문제 - 예제 02. 기초 함수(2)
# 가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. 
# 사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.

# define rectangle()
def rectangle(a, b):
  area = a * b
  perimeter = (a + b) * 2
  return area, perimeter  # tuple 형태로 묶어서 return

width = 20
height = 30
result = rectangle(width, height)
print(result)  # (600, 100)