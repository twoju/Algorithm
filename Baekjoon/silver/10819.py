def recur(arr):
    global ans
    if len(arr) == n:
        s = 0
        for i in range(n-1):
            s += abs(arr[i] - arr[i + 1])
        ans = max(ans, s)
        return
    for i in range(n):
        if visited[i]:
            continue
        arr.append(numbers[i])
        visited[i] = True
        recur(arr)
        visited[i] = False
        arr.pop()


n = int(input())
numbers = sorted(list(map(int, input().split())))
ans = 0
visited = [False] * n
recur([])
print(ans)