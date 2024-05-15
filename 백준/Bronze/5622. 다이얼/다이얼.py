import sys
input = sys.stdin.readline

word = str(input().strip())
ans = 0
for s in word:
    if s in 'ABC':
        ans += 3
    elif s in 'DEF':
        ans += 4
    elif s in 'GHI':
        ans += 5
    elif s in 'JKL':
        ans += 6
    elif s in 'MNO':
        ans += 7
    elif s in 'PQRS':
        ans += 8
    elif s in 'TUV':
        ans += 9
    else:
        ans += 10

print(ans)