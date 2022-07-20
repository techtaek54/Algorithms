n = int(input())
val = n
cycle = 0

while True:

    sum_num = (n // 10) + (n % 10)
    new = int(str(n)[-1] + str(sum_num)[-1])

    n = new
    cycle += 1

    if n == val:
        print(cycle)
        break
