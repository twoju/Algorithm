import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def recur(cur, ans):
    if cur == c:
        if len(ans) == l:
            vo, co = 0, 0
            for a in ans:
                if a in ['a', 'e', 'i', 'o', 'u']:
                    vo += 1
                else:
                    co += 1
                if vo >= 1 and co >= 2:
                    print(ans)
                    return
        return
    recur(cur + 1, ans + arr[cur])
    recur(cur + 1, ans)

l, c = map(int, input().split())
arr = sorted(list(map(str, input().split())))
recur(0, '')