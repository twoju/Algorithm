import sys
sys.stdin = open('3020_bug.txt', 'r')

N, H = map(int, sys.stdin.readline().split())
top = [0] * H 
bottom = [0] * H

for i in range(N):
    height = int(sys.stdin.readline())
    if i % 2 == 0:
        bottom[height - 1] += 1
    else:
        top[height - 1] += 1

for i in range(H - 2, -1, -1):
    top[i] += top[i + 1]
    bottom[i] += bottom[i + 1]

ans = N
cnt = 0
for i in range(H):
    if ans > top[i] + bottom[H - i - 1]:
        ans = top[i] + bottom[H - i - 1]
        cnt = 1
    elif ans == top[i] + bottom[H - i - 1]:
        cnt += 1

print(ans, cnt)

# prefix_num = [0] * H

# num_arr = [int(sys.stdin.readline()) for _ in range(N)]

# for i in range(N):
#     for j in range(num_arr[i]):
#         if i % 2 == 0:
#             prefix_num[H - j - 1] += 1
#         else:
#             prefix_num[j] += 1

# ans = min(prefix_num)
# cnt = 0
# for i in range(H):
#     if prefix_num[i] == ans:
#         cnt += 1

# print(ans, cnt)