# [Codeup 기초 100제] 6095 - 바둑판에 흰 돌 놓기

# input 
n = int(input())  # n : 흰 돌 개수
board = [[0 for _ in range(19)] for _ in range(19)]  # list comprehension => board 초기화

for i in range(n):
  x, y = map(int, input().split())
  board[x-1][y-1] = 1

# output
for i in range(19):
  for j in range(19):
    print(board[i][j], end=' ')
  print()