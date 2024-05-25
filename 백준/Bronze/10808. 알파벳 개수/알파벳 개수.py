import sys
input = sys.stdin.readline

st = input().strip()
cnt=[0] * 26

for i in st:
    cnt[ord(i) - 97] += 1

print(*cnt)