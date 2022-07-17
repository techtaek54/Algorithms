# [KDT1] 파이썬 실습 문제 - 문제 15-2. 문자의 위치 구하기(2)
# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() / index() 사용 X
 
# input
word = input()

# Algorithm
for i in range(len(word)):
  if word[i] == 'a':
    print(i,end=' ')
