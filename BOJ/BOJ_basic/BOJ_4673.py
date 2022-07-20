# self number
# d(33) = 33 + 3 + 3 = 39 -> d(39) = 39 + 3 + 3 =51 ...
# 생성자가 없는 숫자 = 셀프넘버

# 10000 보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력

# 생성자 함수
def constructor_num(n):
    number = n
    for i in str(number):
        number += int(i)
    return number

constructor_list = []

for i in range(1, 10001):
    constructor_list.append(constructor_num(i))

for i in range(1, 10001):
    if i not in constructor_list:
        print(i)
