# 최소 스패닝 트리

"""
크루스칼
-> 간선을 기준으로 합쳐서 트리를 만든다.
제일 가중치가 작은 간선부터 
간선이 연결하는 두 정점이 같은 요소다 : 연결 안함
다른 연결요소다 : 연결함
"""
rnk = [0 for i in range(1000010)]
# 로봇 조립은 size
size = [1 for i in range(1000010)]
parent = [i for i in range(1000010)]

def find(x):
    # 내 루트가 아니면 찾기
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if rnk[a] < rnk[b]:
        parent[a] = b
        size[b] += size[a]
    elif rnk[b] < rnk[a]:
        parent[b] = a
        size[a] += size[b]
    else:
        parent[a] = b
        rnk[b] += 1
        size[b] += size[a]


edge = [list(map)]
edge.sort(key=lambda x:x[-1])

cost = 0

for a, b, c in edge:
    if find(a) != find(b):
        union(a, b)
        cost += c
print(cost)

