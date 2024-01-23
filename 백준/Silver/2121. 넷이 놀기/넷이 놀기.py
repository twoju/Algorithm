import sys
input = sys.stdin.readline

n = int(input().strip())
x_len, y_len = map(int, input().split())

dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort()

def find(f):
    s, e = 0, n - 1
    while s <= e:
        mid = (s + e) // 2
        if dots[mid] == f:
            return True
        elif dots[mid] > f:
            e = mid - 1
        else:
            s = mid + 1
    return False
    

cnt = 0
for i in range(n):
    dx, dy = dots[i][0], dots[i][1]

    if find((dx + x_len, dy)) and find((dx, dy + y_len)) and find((dx + x_len, dy + y_len)):
        cnt += 1

print(cnt)