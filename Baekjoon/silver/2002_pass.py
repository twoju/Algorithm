import sys
sys.stdin = open('2002_pass.txt', 'r')

N = int(sys.stdin.readline())
enter = {}
out = []

for idx in range(N):
    enter[sys.stdin.readline().strip()] = idx

for _ in range(N):
    out.append(sys.stdin.readline().strip())

cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if enter[out[i]] > enter[out[j]]:
            cnt += 1
            break

print(cnt)