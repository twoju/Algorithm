import sys
input = sys.stdin.readline

def recur(cur):
    if cur < 0:
        return True
    if cur == 0:
        return False
    
    if dp[cur] != -1:
        return dp[cur]
    
    cnt = 0
    for i in [1, 3, 4]:
        # 저 사람이 지는 경우가 들어오면 내가 이김
        if not recur(cur - i):
            cnt += 1
        if cnt == 0:
            dp[cur] = False
        else:
            dp[cur] = True
    return dp[cur]
    

n = int(input())
dp = [-1] * 1001
if recur(n):
    print('SK')
else:
    print('CY')