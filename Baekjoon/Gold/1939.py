import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 섬, 중량
island = [i for i in range(10001)]

def find(x):
    # 섬이 내가 노드가 아니면 노드 찾기
    if island[x] != x:
        island[x] = find(island[x])
    # 내가 노드면 섬 리턴
    return island[x]

def union(i, j):
    i = find(i)
    j = find(j) 
    if i > j:
        island[j] = i
    else:
        island[i] = j

edge = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append([-c, a, b])

edge.sort()
first, second = map(int, input().split())

for now in edge:
    weight, a, b = now[0], now[1], now[2]
    weight = abs(weight)
    union(a, b)
    if find(first) == find(second):
        print(weight)
        break