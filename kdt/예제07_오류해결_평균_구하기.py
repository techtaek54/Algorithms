# [KDT1] 파이썬 실습 문제 - 예제 07. [오류해결] 평균 구하기
# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1  # 들여쓰기 위치 틀림 => 더해진 갯수를 의미하는 변수로 분모에 해당 => for문 안으로 이동

print(total // count)  # 산술연산자 /로 수정

# 수정 코드
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)


