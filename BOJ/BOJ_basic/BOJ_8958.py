t = int(input())

for i in range(1, t + 1):
    case = input()
    sum = 0
    score = 0

    for j in case:
        if j == 'X':
            score = 0
            sum += score
        else:
            score += 1
            sum += score
   
    print(sum)
