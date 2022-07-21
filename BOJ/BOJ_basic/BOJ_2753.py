'''
* 윤년 문제
* input : year
* output : 윤년(1) or 윤년X(0)
'''

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(1)
else:
    print(0)