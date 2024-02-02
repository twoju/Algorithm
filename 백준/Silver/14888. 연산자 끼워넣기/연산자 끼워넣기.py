import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
sign = []
for i in range(4):
    if i == 0:
        while brr[i] > 0:
            sign.append('+')
            brr[i] -= 1
    elif i == 1:
        while brr[i] > 0:
            sign.append('-')
            brr[i] -= 1
    elif i == 2:
        while brr[i] > 0:
            sign.append('*')
            brr[i] -= 1
    elif i == 3:
        while brr[i] > 0:
            sign.append('/')
            brr[i] -= 1

def recur(cur, ans):
    global max_a, min_a
    if cur == n:
        max_a = max(max_a, ans)
        min_a = min(min_a, ans)
        return
    for i in range(n - 1):
        if visited[i]:
            continue
        visited[i] = True
        if sign[i] == '+':
            recur(cur + 1, ans + arr[cur])
        elif sign[i] == '-':
            recur(cur + 1, ans - arr[cur])
        elif sign[i] == '*':
            recur(cur + 1, ans * arr[cur])
        else:
            recur(cur + 1, int(ans / arr[cur]))
        visited[i] = False
        
        
visited = [False] * (n - 1)
max_a = -int(1e9)
min_a = int(1e9)
recur(1, arr[0])
print(max_a)
print(min_a)