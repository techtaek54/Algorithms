# [SWEA] D1 - 2027. 대각선 출력하기

for i in range(5):
  for j in range(5):
    if i == j:  # 대각선 = x, y 좌표가 같음
      print('#', end='')
    else:
      print('+', end='')
  print()

