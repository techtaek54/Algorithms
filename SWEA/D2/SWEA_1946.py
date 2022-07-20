import sys

sys.stdin = open('input_1946.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    N = int(input())
    text = ''
    for _ in range(N):
        s = input().split()
        text += s[0] * int(s[1])

    print('#{}'.format(i))
    for j in range(len(text)):
        if (j + 1) % 10 == 0:
            print(text[j])
        else:
            print(text[j], end='')
    print()