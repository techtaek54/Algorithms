'''
- 세는 횟수 : N -> 2N -> 3N -> 4N -> 5N
    - 1 <= N <= 10^6
- 각 회차에서 보게 된 숫자 (중복 => 무시)
- result = [0 ~ 9] => 반복문 종료
     - 조건에 따른 종료 => while문
'''


import sys

sys.stdin = open('input_1288.txt', 'r')

T = int(input())  

for i in range(1, T + 1):
    N = int(input())  
    cnt = 0
    result = []
    while True:
        cnt += 1  
        sheep = N * cnt 
        target = str(sheep)  
        digit = len(target)  
        for j in range(digit):
            if target[j] not in result:
                result.append(target[j]) 
        if len(result) == 10:
            break

    print('#{} {}'.format(i, cnt * N))
        
