import sys
input = sys.stdin.readline

n = int(input().strip())
str_n = str(n)
m = int(input().strip())
buttons = list(map(int, input().split()))

ans = abs(n - 100)

for i in range(1000001):
    for j in str(i):
        if int(j) in buttons:
            break
    else:
        ans = min(ans, abs(n - i) + len(str(i)))

print(ans)