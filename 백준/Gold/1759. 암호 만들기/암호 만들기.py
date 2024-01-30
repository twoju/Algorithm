import sys
input = sys.stdin.readline

l, c = map(int, input().split())
alpha = sorted(list(map(str, input().split())))

vowels = ['a', 'e', 'i', 'o', 'u']

def recur(cur, prev):
    if cur == l:
        vo, co = 0, 0
        for w in res:
            if w in vowels:
                vo += 1
            else: co += 1
        if vo > 0 and co > 1:
            for r in res:
                print(r, end='')
            print('')
        return
    for i in range(prev, c):
        if visited[i]:
            continue
        res[cur] = alpha[i]
        visited[i] = True
        recur(cur + 1, i + 1)
        visited[i] = False

visited = [False] * c
res = [0] * l
recur(0, 0)