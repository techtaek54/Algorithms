# [KDT1] 파이썬 실습 문제 - 예제 04. [오류해결] 입력 받기 2
# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
words = list(map(int, input().split()))  # map() 사용 X, str 공백 구분 => list
print(words)

# 수정 코드
words = input().split()
print(words)
