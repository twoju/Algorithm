import sys
input = sys.stdin.readline

k = int(input().strip())
ans = []
cnt = 0

i = 2
while True:
    if i > int(k ** 0.5):
        break
    if k == 1:
        break
    if k % i == 0:
        ans.append(i)
        cnt += 1
        k = k // i
    else:
        i += 1
    
if k != 1:
    ans.append(k)
    cnt += 1

print(cnt)
print(*ans)