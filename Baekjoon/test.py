import sys
input = sys.stdin.readline

word = input().strip()
ans = 0
for i in range(len(str(word))):
    if word[i] in ['a', 'e', 'i', 'o', 'u']:
        ans += 1

print(ans)