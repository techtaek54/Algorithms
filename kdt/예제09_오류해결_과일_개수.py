# [KDT1] 파이썬 실습 문제 - 예제 09. [오류해결] 과일 개수 구하기
# 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}  # 초기화 방법 오류
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# 수정 코드
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)