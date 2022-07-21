'''
* input : score
* output : grade
* 구간별 조건문 작성
'''

score = int(input())

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score:
    grade = 'B'
elif 70 <= score:
    grade = 'C'
elif 60 <= score:
    grade = 'D'
else:
    grade = 'F'

print(grade)