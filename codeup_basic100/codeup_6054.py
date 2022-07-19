# [Codeup 기초 100제] 6054 - 둘 다 참일 경우만 참 출력하기

a, b = list(map(int, input().split()))

print(bool(a and b))  # and / or 연산자 => 단락평가
