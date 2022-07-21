'''
* 최소, 최대
* I : 정수 n, n개의 정수 case
* O : min, max
'''

n = int(input())
case = list(map(int, input().split()))

print(min(case), max(case))

# min(), max() 직접 구현
min_val = case[0]
max_val = case[0]

for i in range(len(case)):
    if min_val > case[i]:
        min_val = case[i]
    elif max_val < case[i]:
        max_val = case[i]

print(min_val, max_val)