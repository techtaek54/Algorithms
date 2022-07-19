# [Codeup 기초 100제] 6097 - 설탕과자 뽑기

h, w = map(int, input().split())
board = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())

for i in range(n):
  l, d, x, y = map(int, input().split())
  # d == 0 => 막대 가로
  if d == 0:
    for j in range(l):
      board[x-1][y-1+j] = 1
  
  # d == 1 => 막대 세로
  else:
    for j in range(l):
      board[x-1+j][y-1] = 1

# output
for i in range(h):
  for j in range(w):
    print(board[i][j],end=' ')
  print()