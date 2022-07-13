# 초기화
board = []
# 입력
for _ in range(10):
  road = list(map(int, input().split()))
  board += [road]
# 알고리즘
x = y = 1

while True:
  if board[x][y] == 0:
    board[x][y] = 9
  elif board[x][y] == 2:
    board[x][y] = 9
    break
  if board[x+1][y] == 1 and board[x][y+1] == 1:
    break
  if board[x][y+1] != 1:
    y += 1
  elif board[x+1][y] != 1:
    x +=1

# 출력
for i in range(10):
  for j in range(10):
    print(board[i][j],end=' ')
  print()
