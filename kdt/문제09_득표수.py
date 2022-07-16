# [KDT1] 파이썬 실습 문제 - 문제 09. 득표수 구하기
# 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.

# input : list
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# Algorithm
cnt = 0
for student in students:
  if student == '이영희':
    cnt += 1

# output
print(cnt)