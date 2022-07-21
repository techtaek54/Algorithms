'''
- 세 자리 수 끼리의 곱
- 수기로 풀듯 과정 하나씩 전개 
- 각 자릿수에 대해 문자열로 접근 or 수로 접근 가능
'''

a = int(input())
b = int(input())

# str으로 처리, 일부러 반복문 사용하여 복잡하게 풀어봄
b = str(b)
mul_list = []
for i in range(2, -1, -1):
    mul = a * int(b[i])
    mul_list.append(mul)

result = a * int(b)

print(mul_list[0])
print(mul_list[1])
print(mul_list[2])
print(result)

# int로 처리

mul1 = a * (b % 10)  # 1의 자리 
mul2 = a * (b % 100 // 10)  # 10의 자리
mul3 = a * (b // 100)  # 100의 자리

result = a * int(b)  # 위에서 str casting을 했기 때문에 int(b)

print(mul1)
print(mul2)
print(mul3)
print(result)