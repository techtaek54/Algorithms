c = int(input())

for i in range(c):
    case = list(map(int, input().split()))

    avg = sum(case[1:]) / case[0]
    cnt = 0

    for score in case[1:]:
        if score > avg:
            cnt += 1
    
    above_rate = (cnt / case[0]) * 100

    print('{:.3f}%'.format(above_rate))