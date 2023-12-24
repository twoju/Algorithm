import sys
input = sys.stdin.readline

n = int(input())
asis = list(map(int, input().strip()))
tobe = list(map(int, input().strip()))

# (asis -> 변경, tobe -> 비교)
def click(a, b):
    ac = a[:]
    cnt = 0
    for i in range(1, n):
        if ac[i - 1] != b[i - 1]:
            cnt += 1
            for j in range(i - 1, i + 2):
                if j < n:
                    ac[j] = 1 - ac[j]
    if ac == b:
        return cnt
    else:
        return 1e9
    
ans = click(asis, tobe)
asis[0] = 1 - asis[0]
asis[1] = 1 - asis[1]
ans = min(ans, click(asis, tobe) + 1)
if ans != 1e9:
    print(ans)
else:
    print(-1)