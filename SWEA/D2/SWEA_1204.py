# 최빈수 출력
# 최빈수가 2개 이상일 때 => 최대값
import sys

sys.stdin = open('input_1204.txt', 'r')

t = int(input())

for i in range(1, t + 1):
    case_num = int(input())
    case = list(map(int, input().split()))

    # 점수 마다의 통계
    my_dict = {}
    for num in case:
        if num in my_dict:
            my_dict[num] += 1
        else:
            my_dict[num] = 1

    max_count = 0 

    for score, count in my_dict.items():
        if max_count < count:
            max_count = count
            max_score = score
        elif max_count == count:
            if max_score < score:
                max_score = score            

    print('#{} {}'.format(i, max_score))
    


