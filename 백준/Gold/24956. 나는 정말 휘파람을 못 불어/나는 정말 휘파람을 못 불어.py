import sys
input = sys.stdin.readline

n = int(input().strip())
s = input().strip()
ans = 0
arr = [0] * 3
for i in range(n):
    if s[i] == 'W':
        arr[0] += 1
    if s[i] == 'H':
        arr[1] += arr[0]
    if s[i] == 'E':
        ans = (ans * 2 + arr[2]) % 1000000007
        arr[2] += arr[1]

print(ans)