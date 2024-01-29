import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    dots = sorted(list(map(int, input().split())))
                  
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            dist = abs(dots[j] - dots[i])
            target = dots[j] + dist
            s, e = 0, n - 1
            while s <= e:
                mid = (s + e) // 2
                if dots[mid] == target:
                    cnt += 1
                if dots[mid] > target:
                    e = mid - 1
                else:
                    s = mid + 1
    print(cnt)