# 가장 긴 증가하는 부분 수열

n = int(input())
ls = list()
# dp[i] : i 번째 수로 끝나는 증가하는 부분 수열 중 가장 긴 길이를 저장
dp = [1] * n
for i in range(n):
    for j in range(i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

# ---

n = int(input())
ls = list()
# dp[i] : i 번째 수로 끝나는 증가하는 부분 수열 중 가장 긴 길이를 저장
dp = [1] * n
prev = [-1] * n

for i in range(n):
    for j in range(i):
        if ls[j] < ls[i]:
            if dp[i] < dp[j] + 1:
                # dp 값이 갱신 될 때, 어디에서 갱신 되었는지 체크해주기
                dp[i] = dp[j] + 1
                prev[i] = j
mx = -1
idx = 0
for i in range(n):
    if mx < dp[i]:
        mx = dp[i]
        idx = i
print(mx)

# 다시 -1로 돌아갈 때까지 찾아가는 것 : 역추적
while idx != -1:
    print(ls[idx], end=' ')
    idx = prev[idx]