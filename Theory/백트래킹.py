"""백트래킹

n개의 반복문을 표현하는 방법 = 재귀함수

재귀함수 : n중 반복문을 구현하기 위함
for문이 몇개 있을지 모르거나 알아도 입력으로 오는 경우에 사용

**외워야하는 코드** 중복순열, 순열, 조합"""

# 중복순열
def recur(cur):
	if cur == n:   # 멈추는 조건, n중 반복문
		print(*selected)
		return
	for i in range(m):
		selected[cur] = i
		recur(cur + 1)

n, m = map(~
selected = [0] * n
recur(0)

—

# 순열, 방문처리 배열 visited를 활용해서 중복사용 안하고 만들기
def recur(cur):
	if cur == n:   # 멈추는 조건, n중 반복문
		print(*selected)
		return
	for i in range(m):
		if visited[i]:
			continue
		selected[cur] = i
		visited[i] = True
		recur(cur + 1)
		visited[i] = False.  # 재귀 끝나면 꼭 방문 취소 처리 해줘야함

visited = [Fasle] * m
selected = [0] * n

—

# // 조합, 순서도 중요하지 않고 구성이 같으면 같은거다
for i in range(0, m):
	for j in range(i + 1, m):
		for k in range(j + 1, m):
			print(i, j, k)

# 이렇게 하면 되니까 재귀로 해보자

def recur(cur, start):
	if cur == n:   
		print(*selected)
		return
	for i in range(start, m):
		selected[cur] = i
		recur(cur + 1, i + 1)

"""**문제가 12 이하이면 완탐으로 풀어도 된다**

// 다르게 푸는 조합 찾기
** N과 M 시리즈 풀어보기 **
// 가지치기 형식으로 할건지 안할건지 찾기
// 여기서 cur 은 현재 인덱스임"""
def recur(cur, total):
	global ans
	if cur == n:
		if total == k:
			ans +=1
		return
	# 고른 경우
	recur(cur + 1, total + ls[cur])
	# 안고른 경우
	recur(cur + 1, total)

n, m = map()
ls = list(map())

ans = 0
recur(0, 0)
# m이 0인 경우는 빼줘야함
print(ans)

//도영이의 음식
def recur(cur, a, b):
	global ans
	if cur == n:
		ans = min(ans, abs(a - b))
		return
	recur(cur + 1, ..

—
"""2차원에서 백트래킹 하는 법

cur 대신 x, y 로 하고나서 옆으로(y +1) 이동하면서 확인
그리고 y == 벽에 닿으면, x += 1하고 y == 0 해서 다시 확인하면 된다
"""


"""
24.01.30
"""

"""
백트래킹 -> 완탐으로 가능하다

"""

# 1자리인 5진수를 출력 -> 0 1 2 3 4
# 반복문인 경우
for i in range(5):
	print(i)
# 2자리인 5진수를 출력 -> 00 01 02 03 04 .. 44
for i in range(5):
	for j in range(5):
		print(i, j, sep="")

# 순열
def recur(cur):
	if cur == n:
		print(*selected)
		return
	for i in range(m):
		if visited[i]:
			continue
		visited[cur] = i
		recur(cur + 1)

# 중복 조합
def recur(cur, start):
	if cur == n:
		print(*selected)
		return
	for i in range(start, m):
		selected[cur] = i
		recur(cur + 1, i + 1)

# if 조건 바꾸면서 문제 풀기
def recur(cur, start):
	global ans
	if cur == len:
		if sum(selected) == k:
			ans += 1
		return
	for i in range(start, m):
		selected[cur] = i
		recur(cur + 1, i + 1)

"""
24.02.06
백트래킹 2탄

응용하기 편한 형태의 조합을 배운다.
"""

def recur(cur, total):
	if cur == n:
		if total == m:
			cnt += 1
		return
	recur(cur + 1, total + ls[cur])
	recur(cur + 1, total)

recur(0, 0)

# 이런식으로 고를지 안고를지를 재귀로 보내고 원하는만큼 고른 경우만 체크

"""
5 * 5
2차원에서 문제 풀기
"""

def recur(x, y, cnt):
	# 범위 넘어가면 다시 데려오기
	if y == 5:
		x += 1
		y = 0
	# 고름
	recur(x, y + 1, cnt + 1)
	# 안 고름
	recur(x, y + 1, cnt)

