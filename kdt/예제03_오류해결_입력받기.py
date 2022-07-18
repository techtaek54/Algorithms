# [KDT1] 파이썬 실습 문제 - 예제 03. [오류해결] 입력 받기
# 두 수를 Input으로 받아 합을 구하는 코드이다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
numbers = input().split()  
print(sum(numbers))  # 문자열 요소에 sum() 사용 X 

# 수정 코드
numbers = list(map(int, input().split()))  
print(sum(numbers))
