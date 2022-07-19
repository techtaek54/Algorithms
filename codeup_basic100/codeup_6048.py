# [Codeup 기초 100제] 6048 - 정수 2개 입력받아 비교하기1

a, b = list(map(int, input().split()))

ans = 'True' if a < b else 'False'  # 3항 연산자 활용

print(ans)
