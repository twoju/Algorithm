import sys
input = sys.stdin.readline


def recur(cur):
    global ans
    if cur == 5:
        ans = max(ans, sum(res))
        return
    for i in range(len(sorted_exp)):
        if selected[i]:
            continue
        selected[i] = True
        res[cur] = sorted_exp[i][cur]
        recur(cur + 1)
        selected[i] = False


n = int(input().strip())
exp = [list(map(int, input().split())) + [i] for i in range(n)]
res = [0] * 5

ans = 0
sorted_exp = []
visited = [False] * 20001

for i in range(5):
    e = sorted(exp, key=lambda x: x[i], reverse=True)

    cnt = 0
    for j in range(n):
        if cnt == 5:
            break
        if visited[e[j][5]]:
            continue
        visited[e[j][5]] = True
        sorted_exp.append(e[j])
        cnt += 1
        
selected = [False] * len(sorted_exp)

recur(0)
print(ans)