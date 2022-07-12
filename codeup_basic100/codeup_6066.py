num = list(map(int,input().split()))

for i in range(len(num)):
  if num[i] % 2 == 0 : print('even')
  else : print('odd')