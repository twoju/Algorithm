import sys
input = sys.stdin.readline
from collections import defaultdict

def check(cur, prev):
    if cur == m:
        return True
    if d[word[cur]] == 0 or word[cur] == prev:
        d[word[cur]] += 1
        if check(cur + 1, word[cur]):
            return True
    return False

n = int(input().strip())
cnt = 0
for _ in range(n):
    word = input().strip()
    m = len(word)
    d = defaultdict(int)
    if check(0, ''):
        cnt += 1

print(cnt)