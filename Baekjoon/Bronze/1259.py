def isPal(s, e):
    while s < e:
        if arr[s] != arr[e]:
            print('no')
            return
        s, e = s + 1, e - 1
    print('yes')
    return


import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().strip()))
    if len(arr) == 1 and arr[0] == 0:
        break
    isPal(0, len(arr) - 1)