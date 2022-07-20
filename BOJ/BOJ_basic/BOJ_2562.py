case = []
for i in range(9):
    n = int(input())
    case.append(n)

print(max(case))
print(case.index(max(case)) + 1)

# max()를 직접 구현하고, max_index 변수를 만들어 동일한 기능 수행 가능
max_val = case[0]

for i in range(len(case)):
    if max_val < case[i]:
        max_val = case[i]
        max_index = i + 1

print(max_val)
print(max_index)