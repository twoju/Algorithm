import sys
input = sys.stdin.readline

def recur(cur, total):
    if cur == n:
        selected[total] = True
        return
    recur(cur + 1, total + arr[cur])
    recur(cur + 1, total)

n = int(input().strip())
arr = sorted(list(map(int, input().split())))

selected = [False] * 100000001
recur(0, 0)

for i in range(100000002):
    if not selected[i]:
        print(i)
        sys.exit(0)