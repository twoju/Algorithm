import sys

N = int(input())
M = int(input())
ans = abs(100 - N)

if M:
    error = list(map(int, input().split()))
else:
    error = []

for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if str(num[j]) in error:
            break
        elif j == len(num) - 1:
            ans = min(ans, abs(i - N) + len(num))
        
print(ans)