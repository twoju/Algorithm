import sys
input = sys.stdin.readline

n = int(input().strip())
num = list(map(int, input().split()))

pre_sum = [0] * n
pre_sum[0] = num[0]
for i in range(1, n):
    pre_sum[i] = max(num[i], pre_sum[i - 1] + num[i])

print(max(pre_sum))