# 입력값 -> 바둑판 초기화
board = []
for _ in range(19):
  input_board = list(map(int, input().split()))
  board += [input_board]

# 십자 뒤집기 횟수 n
n = int(input())

# 횟수만큼의 좌표 & 알고리즘
for i in range(n):
  x, y = list(map(int, input().split()))
  for j in range(19):
    if board[x-1][j] == 0:
      board[x-1][j] = 1
    else:
      board[x-1][j] = 0
    if board[j][y-1] == 0:
      board[j][y-1] = 1
    else:
      board[j][y-1] = 0

# 출력
for i in range(19):
  for j in range(19):
    print(board[i][j],end=' ')
  print()