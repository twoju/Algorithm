import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input().strip())
strr = list(map(str, input().strip()))
m = len(strr)

d = defaultdict(int)
l, r = 0, 0
ans = 0
while l < m:
    d[strr[r]] += 1
    
    if len(d) > n:
        while l < r:
            if len(d) <= n:
                break
            if d[strr[l]] == 1:
                d.pop(strr[l])
            else:
                d[strr[l]] -= 1
            l += 1
    else:
        ans = max(ans, r - l + 1)
        
    r += 1
    if r >= m:
        break

print(ans)