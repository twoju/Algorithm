import sys
input = sys.stdin.readline

n = int(input().strip())
infos = []
for i in range(n):
    a, b = input().split()
    infos.append((int(a), b, i))

ans = sorted(infos, key=lambda x : (x[0], i))

for i in range(n):
    print(ans[i][0], ans[i][1])