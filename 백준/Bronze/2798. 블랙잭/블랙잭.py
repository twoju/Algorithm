import sys
input = sys.stdin.readline

def recur(cur, selected):
    global ans
    if len(selected) == 3:
        if sum(selected) > m:
            return
        ans = max(ans, sum(selected))
        return
    if cur == n:
        return
    if sum(selected) > m:
        return
    recur(cur + 1, selected + [cards[cur]])
    recur(cur + 1, selected)
    

n, m = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
recur(0, [])
print(ans)