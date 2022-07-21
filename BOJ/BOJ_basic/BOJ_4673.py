'''
* self number 
* I : None
* O : 10000보다 작거나 같은 셀프 넘버, 한 줄에 하나씩
'''
# 생성자 함수
def d(n):
    result = n
    n = str(n)
    for i in range(len(n)):
        result += int(n[i])
    return result

case = []
for i in range(1, 10001):
    case.append(d(i))

for i in range(1, 10000 + 1):
    if i not in case:
        print(i)

# list, for loop로만 풀기
numbers = list(range(1, 10001))
remove_list = []

for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        remove_list.append(num)  # 생성자 리스트 모음

for remove_num in set(remove_list):
    numbers.remove(remove_num)

for i in range(len(numbers)):
    print(numbers[i])