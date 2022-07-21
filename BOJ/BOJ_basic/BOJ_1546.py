'''
* 평균
* I : 과목 개수 n / 현재 성적들 -> list
* O : 주어진 식에 따른 새로운 평균
'''

n = int(input())
case = list(map(int, input().split()))

# m : pick score (max score)
m = max(case)

new_case = []
for i in range(len(case)):
    new_case.append(case[i] / m * 100)

avg = sum(new_case) / len(new_case)

print(avg)

