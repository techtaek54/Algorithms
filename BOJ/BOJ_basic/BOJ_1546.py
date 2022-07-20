n = int(input())
case = list(map(int, input().split()))

m = max(case)
for i in range(len(case)):
    case[i] = case[i] / m * 100

avg = sum(case) / len(case)

print(avg)