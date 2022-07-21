'''
* 최댓값
* I : 한 줄에 하나씩 정수 입력, 9개
* O : 최댓값, 최댓값 인덱스

** 변수 초기화 중요!
'''

case = []

for i in range(9):
    num = int(input())
    case.append(num)

# 함수 사용
print(max(case)) 
print(case.index(max(case)) + 1)

# 함수 사용 X, 반복문 사용
max_val = case[0]
max_idx = 0  # 초기화 필요!

for i in range(len(case)):
    if max_val < case[i]:
        max_val = case[i]
        max_idx = i

print(max_val)
print(max_idx + 1)