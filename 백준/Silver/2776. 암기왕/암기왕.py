# import sys
# input = sys.stdin.readline

# a, b, c = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# brr = sorted(list(map(int, input().split())))
# crr = sorted(list(map(int, input().split())))

# ans = 100000010
# for na in arr:
#     s, e = 0, b - 1
#     diff = 100000010
#     while s < e:
#         mid = (s + e) // 2
#         if abs(brr[mid] - na) < diff:

import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    whole = sorted(list(map(int, input().split())))
    m = int(input().strip())
    see = list(map(int, input().split()))

    for i in range(m):
        if see[i] > whole[-1] or see[i] < whole[0]:
            print(0)
            continue
        s, e = 0, n - 1
        flag = 0
        while s <= e:
            mid = (s + e) // 2
            if whole[mid] == see[i]:
                flag = 1
                break
            if whole[mid] < see[i]:
                s = mid + 1
            else:
                e = mid - 1
        if flag:
            print(1)
        else:
            print(0)