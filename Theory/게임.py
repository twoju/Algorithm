# 게임 문제 특

# 1. 두명이서 게임함
# 2. 둘이 할 수 있는 작업이 동일함
# 3. 턴을 번갈아가면서 진행
# 4. 둘이 최선을 다함
# -> 이길 수 있는 사람이 무조건 고정되어 있음

# 돌게임3
# 내 턴에 1, 3, 4개 남아있으면 내가 무조건 이김
# 내 턴에 2개 남아있으면 내가 무조건 짐
# 전략 : 상대가 지는 패를 주면 내가 이김
# 돌이 x개이면 x-1, x-3, x-4 를 체크해서 지는 패(2)가 하나라도 있으면 내가 이김

def recur(cur): # 내 앞에 돌이 cur 개 있을 때, 최선을 다해 게임한 결과를 리턴
    if cur < 0: # 내 앞에 0개보다 적어? 그러면 상대가 잘못한거니까 내가 이기지
        return True
    if cur == 0:
        return False
    
    if dp[cur] != -1:
        return dp[cur]
    
    cnt = 0
    for i in [1, 3, 4]:
        if not recur(cur - i): # 내가 준게 False 이면 내가 이긴거
            cnt += 1
        if cnt == 0:
            dp[cur] = False
            return dp[cur]
        else:
            dp[cur] = True
            return dp[cur]


n = int(input())
dp = [-1] * (n + 1)
if recur(n):
    print('SK')
else:
    print('CY')


# 프로그래머스 : 사라지는 발판
