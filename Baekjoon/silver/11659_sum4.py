import sys
sys.stdin = open('11659_sum.txt', 'r')

N, M = map(int, sys.stdin.readline().split())

prefix_sum = [0] * (N + 1)

input = list(map(int, sys.stdin.readline().split()))

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + input[i - 1]

for _ in range(M):
    ans = 0
    i, j = map(int, sys.stdin.readline().split())
    ans += prefix_sum[j] - prefix_sum[i - 1]
    print(ans)