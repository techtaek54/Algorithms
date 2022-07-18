# [KDT1] 파이썬 실습 문제 - 예제 06. [오류해결] 1부터 N까지의 2의 곱 저장히기
# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요

# 오류 코드
N = 10
answer = ()  # tuple X => list
for number in range(N + 1):  
    answer.append(number * 2)  # .append() 는 list method
print(answer)

# 수정 코드
N = 10
answer = []
for number in range(N + 1):
  answer.append(number * 2)
print(answer)
