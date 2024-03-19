import sys
input = sys.stdin.readline

n = int(input().strip())
lines = sorted(list(map(int, input().split())))

pre_sum = [0] * n
pre_sum[0] = lines[0]
for i in range(1, n):
    pre_sum[i] = pre_sum[i - 1] + lines[i]

print(sum(pre_sum))