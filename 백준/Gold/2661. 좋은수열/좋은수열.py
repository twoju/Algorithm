import sys
input = sys.stdin.readline

n = int(input().strip())

def check(a):
    for i in range(2, len(a) // 2 + 1):
        if a[-i:] == a[-(2 * i):-i]:
            return False
    return True


def recur(cur, ans, prev):
    if cur == n:
        print(ans)
        sys.exit(0)
    for i in range(1, 4):
        if i == prev:
            continue
        if check(ans + str(i)):
            recur(cur + 1, ans + str(i), i)
    
recur(0, '', 0)