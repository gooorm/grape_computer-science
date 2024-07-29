# 배열(Array) - 백준 10818번 최소, 최대
# 문제 링크: https://www.acmicpc.net/problem/10818
n = int(input())
l = list(map(int, input().split()))
print(f'{min(l)} {max(l)}')
