'''
* 더하기 사이클
    26 : 2 + 6 = 8 => 68 : 6 + 8 = 14 => 84 ...
* I : 정수 n (0 <= n <= 99)
* O : 사이클 cycle
* 조건에 따른 반복문 => while and break
'''

# int로 해석
n = int(input())
copied_n = n
cycle = 0

# 숫자의 길이는 두 자리
while True:
    
    add = (n // 10) + (n % 10)
    new_n = str(n)[-1] + str(add)[-1]
    n = int(new_n)

    if copied_n == n:
        cycle += 1
        break
    cycle += 1

print(cycle)

# str으로 해석

num = input()
origin_num = num
cycle = 0

while True:

    sum = 0

    for i in range(len(num)):
        sum += int(num[i])

    if num[-1] == '0':
        new_num = str(sum)[-1]
    else:
        new_num = num[-1] + str(sum)[-1]
    
    num = new_num
    
    if num == origin_num:
        cycle += 1
        break
    
    cycle += 1

print(cycle)