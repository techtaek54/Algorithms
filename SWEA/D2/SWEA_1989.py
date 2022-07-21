'''
- 회문 : 거꾸로 읽어도 똑같은 단어
- 회문이면 (1) / 아니라면 (0)
- 단어 길이 : 3 <= len(word) <= 10
'''
import sys
sys.stdin = open('input_1989.txt', 'r')

T = int(input())
for i in range(1, T + 1):
    word = input()
    reverse_word = ''
    for j in range(len(word)):
        reverse_word += word[len(word)-1-j]
    if word == reverse_word:
        result = 1
    else:
        result = 0
    print('#{} {}'.format(i, result))
