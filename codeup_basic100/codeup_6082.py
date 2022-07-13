num = int(input())

for i in range(1,num+1):
  # if i%10 in [3,6,9]
  if i % 10 == 3 or i % 10 == 6 or i % 10 == 9: 
    i = 'X'
  print(i,end=' ')

