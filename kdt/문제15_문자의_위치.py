# [KDT1] 파이썬 실습 문제 - 문제 15. 문자의 위치 구하기
# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요. (a가 없는 경우 -1)
# find() / index() 금지

# input
word = input()

# Algorithm
for i in range(len(word)):
  if word[i] == 'a':
    print(i)
    break
else:
  print(-1)