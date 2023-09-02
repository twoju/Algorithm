A, B, D = map(int, input().split())

prime = [False, False] + [True] * (B + 1)

for i in range(2, int(B ** 0.5) + 1):
    if prime[i] == True:
        for j in range(i + i, B + 1, i):
            prime[j] = False

ans = 0
for i in range(A, B + 1):
    if prime[i]:
        if str(D) in str(i):
            ans += 1
print(ans)


