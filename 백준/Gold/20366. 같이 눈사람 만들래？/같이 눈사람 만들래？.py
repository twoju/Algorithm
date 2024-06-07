import sys
input = sys.stdin.readline

n = int(input().strip())
snowball = sorted(list(map(int, input().split())))
ans = 2000000000

for i in range(n - 3):
    for j in range(i + 3, n):
        first = snowball[i] + snowball[j]
        s, e = i + 1, j - 1
        while s < e:
            second = snowball[s] + snowball[e]
            dist = abs(first - second)
            if ans > dist:
                ans = dist
            if first > second:
                s += 1
            else:
                e -= 1
        if ans == 0:
            print(0)
            sys.exit(0)

print(ans)