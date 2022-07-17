# [KDT1] 파이썬 실습 문제 - 문제 18. 알파벳 등장 갯수 구하기
# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

# input
word = input()

# Algorithm (1) - if-else 사용
basket = {}
for i in range(len(word)):
   if word[i] in basket:
      basket[word[i]] += 1
   else:
      basket[word[i]] = 1

# Algorithm (2) - .get() method 사용
basket = {}
for i in range(len(word)):
   basket[word[i]] = basket.get(word[i], 0) + 1


# output
for c in basket:
   print(c, basket[c])
