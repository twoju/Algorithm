import sys
input = sys.stdin.readline

arr = input().strip()
if arr == arr[::-1]:
    print(1)
else:
    print(0)