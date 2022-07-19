# [Codeup 기초 100제] 6058 - 둘 다 거짓일 경우만 참 출력하기

a, b = list(map(int, input().split()))

print(not bool(a) and not bool(b))