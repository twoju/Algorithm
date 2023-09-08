import sys
sys.stdin = open('3020_bug.txt', 'r')

N, H = map(int, sys.stdin.readline().split())

prefix_num = [0] * H

num_arr = [int(sys.stdin.readline()) for _ in range(N)]

for i in range(N):
    for j in range(num_arr[i]):
        if i % 2 == 0:
            prefix_num[H - j - 1] += 1
        else:
            prefix_num[j] += 1

cnt = 0
for i in range(H):
    if prefix_num[i] == min(prefix_num):
        cnt += 1

print(min(prefix_num), cnt)