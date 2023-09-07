import sys
sys.stdin = open('2559_str.txt', 'r')

N, K = map(int, sys.stdin.readline().split())

arr = [i for i in map(int, sys.stdin.readline().split())]

prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

ans = -100 * K
for i in range(N - K + 1):
    ans = max(ans, prefix_sum[i + K] - prefix_sum[i])

print(ans)