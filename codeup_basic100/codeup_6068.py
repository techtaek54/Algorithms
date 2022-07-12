score = int(input())

if 90 <= score <= 100: result = 'A'
elif 70 <= score < 90: result = 'B'
elif 40 <= score < 70: result = 'C'
else: result = 'D'

print(result)