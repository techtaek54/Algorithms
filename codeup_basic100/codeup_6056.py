# [Codeup 기초 100제] 6056 - 참/거짓이 서로 다를 때에만 참 출력하기

a, b = list(map(int, input().split()))

print(bool(a) != bool(b))