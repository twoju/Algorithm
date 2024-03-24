import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    a = int(input().strip())
    if a <= k:
        coins.append(a)
        
coins.sort(reverse=True)
ans = 0

for i in range(len(coins)):
    if k >= coins[i]:
        ans += k // coins[i]
        k = k % coins[i]

print(ans)