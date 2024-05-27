import sys
input = sys.stdin.readline

n = input().strip()
visited = [0] * 10
for i in n:
    if i == '9':
        visited[6] += 1
    else:
        visited[int(i)] += 1

ans = 0
for i in range(10):
    if i == 6:
        res = visited[i] // 2
        if visited[i] % 2:
            res += 1
        ans = max(ans, res)
    else:
        ans = max(ans, visited[i])

print(ans)