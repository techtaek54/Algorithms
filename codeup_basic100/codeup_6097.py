# 입력 : 가로(w), 세로(h) -> board 초기화
h,w  = list(map(int, input().split()))
board = [[0 for _ in range(w)] for _ in range(h)]

# 입력 : 막대 개수(n)
n = int(input())

# 입력 : 막대길이(l), 방향(d), 좌표(x,y) -> 알고리즘
# d : 가로(0), 세로(1)
for _ in range(n):
  l, d, x, y = list(map(int, input().split()))
  if d == 0:
    for i in range(l):
      board[x-1][y-1+i] = 1
  if d == 1:
    for i in range(l):
      board[x-1+i][y-1] = 1 
# 출력
for i in range(h):
  for j in range(w):
    print(board[i][j],end=' ')
  print()