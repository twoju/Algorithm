import sys
input = sys.stdin.readline

n = int(input())

num_list = [0 for _ in range(10001)]
for _ in range(n):
    cur = int(input())
    num_list[cur] += 1

for i in range(10001):
    if i != 0:
        for _ in range(num_list[i]):
            print(i)