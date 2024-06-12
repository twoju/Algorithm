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

n = int(input().strip())
nrr = sorted(list(map(int, input().split())))
m = int(input().strip())
mrr = list(map(int, input().split()))

for a in mrr:
    flag = 0
    s, e = 0, n - 1
    while s <= e:
        mid = (s + e) // 2
        if a == nrr[mid]:
            flag = 1
            break
        if a < nrr[mid]:
            e = mid - 1
        else:
            s = mid + 1

    if flag:
        print(1)
    else:
        print(0)