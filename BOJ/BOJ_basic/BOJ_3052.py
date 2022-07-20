case = []
for i in range(10):
    num = int(input())
    case.append(num % 42)

# 중복제거를 위한 set() 활용
rest = len(set(case))
print(rest)    

# set() 없이 중복제거
rest_list = []
for val in case:
    if val in rest_list:
        continue
    rest_list.append(val)
print(len(rest_list))