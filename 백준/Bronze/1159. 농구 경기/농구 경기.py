import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input().strip())

names = defaultdict(list)

for _ in range(n):
    name = str(input().strip())
    names[name[0]].append(name)

ans = ''

sorted_names = dict(sorted(names.items()))

for name in sorted_names.values():
    if len(name) >= 5:
        ans += name[0][0]

if ans == '':
    print('PREDAJA')
else:
    print(ans)