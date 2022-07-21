'''
* OX 퀴즈
* I : test case T / score
* O : 점수로 환산하여 출력
'''

T = int(input())

for i in range(T):
    score = input()
    point = 0
    result_score = 0

    for j in range(len(score)):
        
        if score[j] == 'O':
            point += 1
        else:
            point = 0
        
        result_score += point
        
    print(result_score)