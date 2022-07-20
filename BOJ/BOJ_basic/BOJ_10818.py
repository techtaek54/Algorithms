n = int(input())
case = list(map(int, input().split()))

print(min(case), max(case))

# min() / max() 구현
min_val = case[0]
max_val = case[0]

for i in range(len(case)):
    if min_val > case[i]:
        min_val = case[i]
    if max_val < case[i]:
        max_val = case[i]
print(min_val, max_val)
