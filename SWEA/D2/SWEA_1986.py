import sys

sys.stdin = open('input_1986.txt', 'r')

t = int(input())

for i in range(1, t + 1):
    sum = 0
    n = int(input())
    for j in range(1, n + 1):
        if j % 2 == 0:
            sum -= j
        else:
            sum += j
    print('#{} {}'.format(i, sum))