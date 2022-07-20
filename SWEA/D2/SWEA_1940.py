import sys

sys.stdin = open('input_1940.txt', 'r')

t = int(input())

for i in range(1, t + 1):
    # command 갯수
    n = int(input()) 
    speed = 0
    distance = 0

    for j in range(n):
        command = list(map(int, input().split()))
        if command[0] == 1:
            speed += command[1]
        elif command[0] == 2:
            if speed < command[1]:
                speed = 0
            else:
                speed -= command[1]

        distance += speed

    print('#{} {}'.format(i, distance))