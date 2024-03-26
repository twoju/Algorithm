"""
트리의 정의
1. 모든 노드가 하나의 연결요소 (그래프를 구성하는 연결요소의 개수가 한개)
2. 사이클이 없는 그래프
3. 간선의 개수 == 노드의 개수 - 1

또는 모든 정점에서 다른 모든 정점으로 가는 단순 경로가 정확히 하나인 그래프

사이클이 없는 그래프는
각각의 연결 요소가 트리이고 묶어서 포레스트 라고 부름

Rooted Tree

하나의 노드를 잡고 끌어 올리면 그 노드가 루트

루트 아래에서 또 하나의 노드를 기준으로 트리가 있으면 서브트리
"""

"""
11725번 트리의 부모 찾기
트리의 루트가 1일 때 각 노드의 부모 찾기
-> 그냥 그래프인데 1인 노드를 들어올려서 루트 1인 트리가 되는것
"""

# 루트에서부터 dfs 를 타면 무조건 자식 방향으로밖에 갈 수 없음
def dfs(cur):
    visited[cur] = True
    for nxt in graph[cur]:
        if visited[nxt]:
            continue
        dfs(nxt)


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(n - 1):
    a, b = map
    graph[a].append(b)
    graph[b].append(a)


# 트리는 사이클이 없기 때문에 무한루프가 발생하지 않음
# 이전 노드를 저장하고 그 곳으로만 안가면 된다
# 트리는 사이클이 없으니까 이전만 안가면 되고 방문처리가 필요없음
def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        dfs(nxt)
        

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map
    graph[a].append(b)
    graph[b].append(a)


"""
1. 각 노드의 부모노드 찾기
2. 각 노드의 깊이(level)
3. 각 노드의 서브트리의 크기
"""

# 1. 부모노드 찾기는 parent
def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        # 내 다음 노드의 부모는 나다
        parent[nxt] = cur
        dfs(nxt)
        

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map
    graph[a].append(b)
    graph[b].append(a)

# 2. 깊이 구하기
def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        # 내 다음 노드의 부모는 나다
        parent[nxt] = cur
        # 너(자식)의 깊이는 내 깊이보다 하나 밑이다
        # dfs 보다 이전에 적어야함 **꼭**
        depth[nxt] = depth[cur] + 1
        dfs(nxt)
        

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
depth = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map
    graph[a].append(b)
    graph[b].append(a)


# 3. 서브트리의 크기
def dfs(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        # 내 다음 노드의 부모는 나다
        parent[nxt] = cur
        # 너(자식)의 깊이는 내 깊이보다 하나 밑이다
        # dfs 보다 이전에 적어야함 **꼭**
        depth[nxt] = depth[cur] + 1
        dfs(nxt)
        # 자식의 dfs를 계산하고 있으면 하나씩 올려가면서 부모의 크기 구함
        size[cur] += size[nxt] # 트리 dp
        

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
depth = [0] * (n + 1)
# 처음에 크기를 모두 1로 초기화
size = [1] * (n + 1)
for _ in range(n - 1):
    a, b = map
    graph[a].append(b)
    graph[b].append(a)

"""
회사문화
"""

def dfs(cur):
    for nxt in graph[cur]:
        # 내 자식 nxt 에게 내 점수를 물려주다
        score[nxt] += score[cur] # 트리 dp
        dfs(nxt)

graph = [[] for _ in range()]
score = [0] * (n + 1)
for i in range(1, n):
    # 부모에서 자식으로만 향하도록 만들기 (확실한 상하관계니까)
    graph[ls[i]].append(i + 1)

for _ in range(m):
    a, b = map
    score[a] += b

dfs(1)
print(score[1:])

"""
# dfs 위에서 불러오면 부모의 정보를 자식에게 주는 것
dfs(nxt)
# 밑에서 불러오면 자식의 정보를 부모에게 주는 것

재귀함수 디폴트 깊이는 1000
sys.setrecursionlimit(10 ** 6)

트리의 지름은
아무나 잡고 올리기
그거 기준으로 제일 먼 노드 찾고
그 노드에서 dfs 해서 또 제일 먼 노드 찾기
그 거리가 트리의 지름
"""

"""
싸이클 찾기
"""
if depth[nxt] == 0:
    depth[nxt] = depth[cur] + 1
    dfs(nxt, cur)
elif depth[nxt] < depth[cur]:
    sz = depth[cur] - depth[nxt] + 1

"""
사이클이 정확히 1개인 그래프
정점이 N개 간선이 N개 인 경우
사이클인 정점이랑 아닌 정점 판별하기
bfs로 가능
"""

n = int(input())
graph = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)     # 차수
for _ in range(n):
    a, b = map()
    graph[a].append(b)
    graph[b].append(a)
    deg[a] += 1
    deg[b] += 1

from collections import deque

q = deque()
cycle = [True] * (n + 1)
for i in range(1, n + 1):
    # 차수가 1이면 그건 사이클이 없는 노드임
    if deg[i] == 1:
        q.append(i)
        cycle[i] = False

while q:
    x = q.popleft()
    for nxt in graph[x]:
        deg[nxt] -= 1
        if deg[nxt] == 1 and cycle[nxt]:
            q.append(nxt)
            cycle[nxt] = False