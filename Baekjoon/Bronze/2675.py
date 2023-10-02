T = int(input())
for _ in range(T):
    R, arr = input().split()
    arr = list(arr)
    ans = ''
    for i in arr:
        for _ in range(int(R)):
            ans += i
    print(ans)