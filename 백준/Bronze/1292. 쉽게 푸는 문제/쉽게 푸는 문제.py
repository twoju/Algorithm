import sys
input = sys.stdin.readline

a, b = map(int, input().split())
li = []
if a == 1 and b == 1:
    print(1)
else:
    for i in range(1, b):
        for _ in range(i):
            li.append(i)
    print(sum(li[a-1:b]))