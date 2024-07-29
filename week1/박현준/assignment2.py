# 배열(Array) - 백준 8958번 OX퀴즈
# 문제 링크: https://www.acmicpc.net/problem/8958
num = int(input())
for _ in range(num):
    caseList = list(input().split('X'))
    score = 0
    for case in caseList:
        if 'O' in case:
            for i in range(1, len(case) + 1):
                score += i
    print(score)
