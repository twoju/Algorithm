"""탑다운 DP

퇴사2"""

def recur(cur):  # 현재 cur 일이고, 앞으로 최선을 다해서 일을 고를 때 얻을 수 있는 최대 이득
	if cur > n:
		return -123123123123123
	if cur == n: # 퇴사하는 날이니까 더이상 일하지 말고 퇴사 ㄱ
		return 0
	if dp[cur] != -1: # 똑같은 인자에 대해서 항상 같은 값을 저장했다가 뱉는 경우에 저장해서 사용
		return dp[cur]
	dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
	return dp[cur]

n = ,,
arr = ,,
dp = [-1] * n
print(recur(0))

# RGB 거리


# 백트로 풀어보기
def recur(cur, total, prev):
	global ans
	if cur == n:
		ans = min(ans, total)
		return
	for i in range(3):
		if i == prev:
			continue
		recur(cur + 1, total + ls[cur][i], i)


n = int(input())
ls = [list ]
ans = int(1e9)
"""
탑다운 dp 짜는 법
1. 백트를 짠다
2. 리턴하는 방식으로 바꾼다 (처음부터 이걸로 해도 됨)
3. 메모이제이션"""


def recur(cur, prev):
	global ans
	if cur == n: # 앞으로 칠하는 비용은 더이상 안든다
		return 0

	# 한번 구한 것은 다시 구하지 않는다는 표시
	if dp[cur][prev] != -1:
		return dp[cur][prev]
	ret = int(le9)
	for i in range(3):
		if i == prev:
			continue
		ret = min(ret, recur(cur + 1, i) + ls[cur][i])
	dp[cur][prev] = ret
	return dp[cur][prev]

dp = [[-1] * 3 for _ in range(n)]


평범한 배낭

백트로 해보자

def recur(cur, w, total):
	global ans
	if w > m:
		return
	if cur == n:
		ans = max(ans, total)
		return
	recur(cur + 1, w + ls[cur][0], total + ls[cur][1])
	recur(cur + 1, w, total)
"""
-> 이렇게하면 답은 맞지만 시간초과임
-> 경우의 수가 많으니까 dp 해야겠당
-> return 으로 바꿔야지"""

def recur(cur, w):
	if w > m:
		return -123123123123
	if cur == n:
		return 0
	# 같은 cur 과 w가 들어왔을 때 똑같은 값을 뱉는다는 확신이 들면 메모이제이션 고
	if dp[cur][w] != -1:
		return dp[cur][w]
	dp[cur][w] = max(recur(cur + 1, w + ls[cur][0]) + ls[cur][1], recur(cur + 1, w))
	return dp[cur][w]


dp = [[-1] * 101010 for _ in range(n)]