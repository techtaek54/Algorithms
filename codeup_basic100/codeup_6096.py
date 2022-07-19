# [Codeup 기초 100제] 6096 - 바둑알 십자 뒤집기

# input
board = [[0 for _ in range(19)] for _ in range(19)]
for i in range(19):
  board[i] = list(map(int, input().split()))

n = int(input())

for i in range(n):
  x, y = map(int, input().split())
  for j in range(19):
    if board[x-1][j] == 1:
      board[x-1][j] = 0
    else:
      board[x-1][j] = 1

    if board[j][y-1] == 1:
      board[j][y-1] = 0
    else:
      board[j][y-1] = 1

# output
for i in range(19):
  for j in range(19):
    print(board[i][j],end=' ')
  print()
