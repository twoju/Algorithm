import sys
input = sys.stdin.readline

t = int(input().strip())
pref_sum = [0] * 1000010
pref_sum[0] = 1
for i in range(1, 1000010):
    pref_sum[i] = pref_sum[i - 1] + str(i).count('0')

for _ in range(t):
    n, m = map(int, input().split())
    if n == 0:
        print(pref_sum[m])
    else:
        print(pref_sum[m] - pref_sum[n - 1])