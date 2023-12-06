"""
Disjoint set (물리집합)

용도 : 연결 요소의 정보 저장

1717 집합의 표현
(union find, disjoint set, 분리 집합 등등)

루트가 같으면 같은 트리(집합)

구현할 함수
find(x): x가 속한 트리의 루트를 구하는 함수
union(a, b) : 
"""

# 효율적이진 않지만 기본 코드 구현

# 자기 자신이 루트가 되도록 먼저 만들기
parent = [i for i in range(1000010)]

def find(x):
    # 내 부모가 나인 경우
    if parent[x] == x:
        return x
    return find(parent[x])


# 시간 복잡도 == find의 시간 복잡도와 같다.
# 그러므로 find를 최적화 하면 union도 알아서 빨라짐
def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a


n, m = map()

for _ in range(m):
    oper, a, b = map()
    if oper == 1:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')
    else:
        union(a, b)

"""
union find 최적화 두 가지
: 일자 형태로 편향된 트리를 만들지 않기 위함

1. 경로 압축
-> find 함수에서 진행
2. union by rank
-> union 함수에서 진행 but find를 최적화 하기 위해 진행하는 것이다.
"""

# 경로 압축
# 어차피 타고 올라가면 루트니까 중간을 제거하고 바로 루트에 붙임
# 시간 복잡도 : amortized O(logN) 
"""
amortized : 분할상환
예시 : python list append : O(1)
한 번이 실제로 O(N)은 아니지만 N번 했을 때는 한 번이 O(1)이다

즉 amortized O(logN) 이면 한 번은 O(N)일 수 있지만 N번 하면 O(logN)이다
"""
def find(x):
    # 내 루트가 아니면 찾기
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# union by rank
"""
small to large (작은 집합에서 큰 집합으로 합치는 테크닉)
두 개의 집합을 합칠 때, 작은 집합을 큰 집합 쪽으로 합치는게 더 효율적임
O(logN) -> O(NlogN)

깊이도 큰 애한테 작은 애가 붙는 것이 좋다. 
왜냐하면 큰 애한테 붙으면 그 깊이 안에서 트리가 추가지만 작은애한테 붙으면 깊이가 늘어나야하기 때문.
"""
rnk = [0 for i in range(1000010)]
# 로봇 조립은 size
size = [1 for i in range(1000010)]

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

