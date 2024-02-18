import sys
input = sys.stdin.readline

def recur(cur):
    if cur > 1:
        return (cur * recur(cur - 1))
    else:
        return 1

t = int(input().strip())

for _ in range(t):
    n, m = map(int, input().split())
    print(recur(m) // (recur(m - n) * recur(n)))