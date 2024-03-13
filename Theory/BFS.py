"""
BFS, 다익스트라

출발점에서 몇 번째로 갈 수 있는 점인지를 확인함
재귀를 사용하지 않음

Queue 로 구현함

Queue 에 하나를 넣고, 빼면서 연결된 것 중 방문하지 않은 것을 넣음
여러개면 여러개 넣기
없으면 끝

바이러스를 BFS로 구현
파이썬은 import deque 사용

겹치는 숫자가 있는 경우에는 하나만 들어가야함
방문처리를 queue 에서 뺄 때 하면 안된다

최단 경로를 구할 때 BFS (가중치가 0~1 일 때, 간선 수 세기)
다익스트라 : 음수 가중치 없을 때
"""
import deque

graph = [[] for _ in range(n + 1)]
for 인접리스트 생성

q = deque()
visited = [False] * (n + 1)
q.append(n)
# *** queue에 넣는거랑 방문체크는 세트임 ***

while q:
    cur = q.pop()


"""
1. 거리배열
dist 에 갈 수 있는 거리를 저장하겠다.

"""
# 숨바꼭질

visited = [False] * 101010
q = deque()
q.append(n)
# 시작점 표시
visited[n] = True
dist = [0] * 101010

while q:
    cur = q.popleft()
    for nxt in [cur - 1, cur + 1, cur * 2]:
        # 범위부터 보기
        if nxt < 0 or nxt > 101010:
            continue
        if visited[nxt] :
            continue
        # 넣으면서 방문체크!!
        q.append(nxt)
        # 지금에서 한 칸 더 가는거니까 + 1
        dist[nxt] = dist[cur] + 1 
        visited[nxt] = True


# dist 사용 안하는 버전
"""
2. 큐에 거리 같이 저장하기
"""

visited = [False] * 101010
q = deque()
q.append((n, 0))
# 시작점 표시
visited[n] = True

while q:
    cur, dist = q.popleft()
    if cur == k:
        print(dist)
        break
    for nxt in [cur - 1, cur + 1, cur * 2]:
        # 범위부터 보기
        if nxt < 0 or nxt > 101010:
            continue
        if visited[nxt] :
            continue
        # 넣으면서 방문체크!!
        q.append((nxt, dist + 1))
        visited[nxt] = True

"""
3. 깊이 단위로 끊어서 탐색
"""

# 한 번 할 때마다 한 queue 층씩 확인 가능하다
for _ in range(len(q)):
    cur = q.popleft()
    for nxt in [cur - 1, cur + 1, cur * 2]:
        # 범위부터 보기
        if nxt < 0 or nxt > 101010:
            continue
        if visited[nxt] :
            continue
        # 넣으면서 방문체크!!
        q.append(nxt)
        visited[nxt] = True

# 그래서 queue가 빌때까지 하는데
# 한 층이 끝날 때마다 dist += 1 해주면 층을 구할 수 있음
dist = 0
while q:
    cur = q.popleft()
    for nxt in [cur - 1, cur + 1, cur * 2]:
        # 범위부터 보기
        if nxt < 0 or nxt > 101010:
            continue
        if visited[nxt] :
            continue
        # 넣으면서 방문체크!!
        q.append(nxt)
        visited[nxt] = True
    dist += 1

    # 만약 거리가 3인 깊이까지만 탐색하고 싶은 경우
    if cur == k:
        print(dist)
        break
    # 이렇게 활용 가능
    # -> 미로 탐색, 벽 부수고 이동하기

"""
다익스트라
"""
import heapq

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    dist[x] = 0
    while q:
        dist_x, x = heapq.heappop(q)
        if dist_x != dist[x]:
            continue
        for u, weight in graph[x]:
            if dist[u] > dist[x] + weight:
                dist[u] = dist[x] + weight
                heapq.heappush(q, (dist[u], u))

dist = [int(1e9)] * (n + 1)
for _ in range(m):
    a, b, c = map()
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(start)

for i in range(1, n + 1):
    print(dist[i] if dist[i] != int(1e9) else 'INF')


"""
BFS, dijkstra 좀 어려운 경우

1. 더미노드 (토마토: 시작점이 여러개)
- 가상의 한 정점을 만들고, 거기에서 여러 시작 노드가 연결 된 것 처럼해서
한 번에 큐에 넣을 수 있도록 한다

2. 시작점이랑 도착점 바꾸기
(BFS는 시작점부터 다른 모든 정점까지의 최단 거리를 구하는 것)
- 도착점은 1개인데 시작점이 여러개인 경우

3. 간선 방향 바꾸기
- 단방향 그래프인 경우

4. 구현이 어려운 경우
"""

"""
바이러스 문제
"""

n = int(input().strip())
m = int(input().strip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
q = deque()
q.append(1)
visited[1] = True

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if visited[nxt]:
            continue
        q.append(nxt)
        visited[nxt] = True

# ---
dist = 0
size = len(q)
# 거리가 3인 곳 까지만 가고싶은 경우는 while q 대신 range(3)
for _ in range(3):
    for _ in range(size):
        cur = q.popleft()
        if cur == m:
            print(dist)
            break
        for nxt in [cur - 1, cur + 1]:
            if visited[nxt]:
                continue
            q.append(nxt)
            visited[nxt] = True
    dist += 1

# ---

# dijkstra 사용법
    
while q:
    dist_x, x = heapq.heappop(q)
    if dist_x != dist[x]:
        continue
    for u, w in graph[x]:
        if dist[u] > dist[x] + w:
            dist[u] = dist[x] + w
            heapq.heappush(q, (dist[u], u))

        