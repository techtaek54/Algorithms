n = int(input())

# (x,y) : 0~18 / size : 19 X 19 
board = [[0 for _ in range(19)]for j in range(19)] 

for _ in range(n):
  x, y = list(map(int,input().split()))
  board[x-1][y-1] = 1


for i in range(19):
  for j in range(19):
    print(board[i][j],end=' ')
  print()
  