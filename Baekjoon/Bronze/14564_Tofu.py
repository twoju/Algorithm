# 1
# 5
# 2
# 5
# 4
# 6
# 0

import sys
sys.stdin = open('14564_Tofu.txt', 'r')
# N = 인원수, M = 두부 모 수, A = 주최자 번호
N, M, A = map(int, sys.stdin.readline().split())
center = M // 2 + 1
for _ in range(M):
    diff = abs(A - center)
    call = int(sys.stdin.readline().strip())
    if call == center:
        print(0)
    else:
        if (call + diff) >= N:
            print(call, N - call + diff)
            A = N - call + diff
        else:
            print(call, call + diff)
            A = call + diff
    
# now 가 본인을 부르는 경우에 지는데 이거는 고려 안하나?