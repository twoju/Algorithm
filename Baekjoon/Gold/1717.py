import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(1000010)]

def find(x):
    # 같은 집합(루트가 같은지) 확인
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

for _ in range(m):
    tp, a, b = map(int, input().split())
    if tp == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)