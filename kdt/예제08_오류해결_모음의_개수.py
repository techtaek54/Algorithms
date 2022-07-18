# [KDT1] 파이썬 실습 문제 - 예제 08. [오류해결] 모음의 개수 찾기
# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u":  # 해당 조건문은 계속 True
        count += 1

print(count)

# 수정 코드
word = "HappyHacking"

count = 0

for char in word:
    # char == 'a' or char == 'e' or ... or char == 'u': 로도 수정 가능
    if char in 'aeiou':
        count += 1

print(count)