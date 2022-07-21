'''
* I : test case C / 학생수 n, case -> list
* O : 평균을 넘는 학생들의 비율
'''

C = int(input())

for i in range(C):
    case = list(map(int, input().split()))
    n = case[0]
    score = case[1:]
    avg = sum(score) / n
    cnt = 0

    for s in score:
        if s > avg:
            cnt += 1
    
    above_rate = cnt / n * 100
    
    print('{:.3f}%'.format(above_rate))
