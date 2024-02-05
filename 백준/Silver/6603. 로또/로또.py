import sys
input = sys.stdin.readline

def recur(cur, prev):
    if cur == 6:
        print(*ans)
        return
    for nxt in range(prev + 1, len(nums)):
        ans[cur] = nums[nxt]
        recur(cur + 1, nxt)


while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        sys.exit(0)
    nums = sorted(arr[1:])

    ans = [0] * 6
    recur(0, -1)
    print('')