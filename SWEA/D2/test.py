for i in range(0, 63):
    bin_num = bin(i)[2:]
    msg = ''
    while len(bin_num) < 6 :
            bin_num = '0' + bin_num
    msg += bin_num
    print(msg)
