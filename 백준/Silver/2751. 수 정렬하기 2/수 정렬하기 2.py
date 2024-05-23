import sys
input = sys.stdin.readline

n = int(input().strip())
li = []
for _ in range(n):
    a = int(input().strip())
    li.append(a)

li.sort()

for i in li:
    print(i)