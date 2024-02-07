import sys
input = sys.stdin.readline

def recur(cur):
    global cnt
    if cur == 10:
        if len(ans) == 10:
            score = 0
            for i in range(10):
                if answer[i] == ans[i]:
                    score += 1
                if score > 4:
                    cnt += 1
                    return
        return
    for i in range(1, 6):
        if cur > 1 and len(ans) > 1:
            if ans[cur - 2] == ans[cur - 1] == i:
                continue
        ans[cur] = i
        recur(cur + 1)
        ans[cur] = 0

    
answer = list(map(int, input().split()))
cnt = 0
ans = [0] * 10
recur(0)
print(cnt)