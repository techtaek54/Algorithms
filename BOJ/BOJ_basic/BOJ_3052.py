'''
* I : 한 줄에 하나씩 정수 n (0 <= n <=1000)
* O : 42로 나누었을 때, 서로 다른 나머지 갯수
    * 중복 제거 => set()
'''

case = []
for i in range(10):
    case.append(int(input()) % 42)

rest_case = set(case)

print(len(rest_case))

# set() 구현
set_case = []
for i in range(len(case)):
    if case[i] not in set_case:
        set_case.append(case[i])

# len() 구현
cnt = 0

for i in set_case:
    cnt += 1

print(cnt)



