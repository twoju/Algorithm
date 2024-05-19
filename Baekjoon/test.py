import sys
input = sys.stdin.readline

def recur(cur, now, prev):
    if prev + k < cur:
        return
    if cur == n:
        print(now % 2)
        return
    if cur in block:
        recur(cur + 1, now, prev)
    recur(cur + 1, now + 1, cur)
    recur(cur + 1, now, prev)
    
    

n, k = map(int, input().split())
block = list(map(int, input().split()))
recur(0, 0, 0)
