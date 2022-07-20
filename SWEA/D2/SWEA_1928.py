import sys

sys.stdin = open('input_1928.txt', 'r')
decode_table = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        '0','1','2','3','4','5','6','7','8','9','+','/'
        ]

t = int(input())

for i in range(1, t + 1):
    text = input()
    msg = ''
    for j in range(len(text)):
        num = decode_table.index(text[j])
        bin_num = bin(num)[2:]

        while len(bin_num) < 6 :
            bin_num = '0' + bin_num
        msg += bin_num
    
    result = ''
    for k in range(len(text) * 6 // 8):
        ans = int(msg[k * 8 : k * 8 + 8], 2)
        result += chr(ans)
    print('#{} {}'.format(i, result))
