import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
idx = blocks.index(max(blocks))

total = 0

left = 0
for i in range(idx):
    left = max(left, blocks[i])
    if blocks[i] < left:
        total += left - blocks[i]

right = 0
for i in range(w - 1, idx, -1):
    right = max(right, blocks[i])
    if blocks[i] < right:
        total += right - blocks[i]

print(total)