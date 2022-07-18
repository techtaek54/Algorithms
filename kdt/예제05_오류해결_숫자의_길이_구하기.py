# [KDT1] 파이썬 실습 문제 - 예제 05. [오류해결] 숫자의 길이 구하기
# 아래 코드는 숫자의 길이를 구하는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
number = 22020718 
print(len(number))  # len(numeirc type X) => len(iterable) 

# 수정 코드
number = str(22020718)
print(len(number))