# [KDT1] 파이썬 실습 문제 - 문제 01. 수 구분하기
# 주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.

# input : str -> int
n = int(input())

# Algorithm : 3항 연산자
ans = '참' if (n % 3 == 0) and (n % 2 == 0) else '거짓'

# output : str
print(ans)