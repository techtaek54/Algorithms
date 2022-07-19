# [Codeup 기초 100제] 6098 - 성실한 개미

# input
board = []
for i in range(10):
  case = list(map(int, input().split()))
  board.append(case)

# Algorithm
x = 1
y = 1

while True:
  # 지나간 흔적 and  종료상황1
  if board[x][y] == 0:
    board[x][y] = 9
  elif board[x][y] == 2:
    board[x][y] = 9
    break
  
  # 종료상황 2
  if board[x][y+1] == 1 and board[x+1][y] == 1:
    break

  # 이동 조건
  if board[x][y+1] == 1:
    x += 1
  else:
    y += 1

# output
for i in range(10):
  for j in range(10):
    print(board[i][j],end=' ')
  print()