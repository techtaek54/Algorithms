a = int(input())  # 세 자리 수
b = int(input())  # 세 자리 수

ans1 = a * (b % 100 % 10) 
ans2 = a * (b % 100 // 10)
ans3 = a * (b // 100)
result = (ans1 + (ans2 * 10) + (ans3 * 100))

print(ans1)
print(ans2)
print(ans3)
print(result)