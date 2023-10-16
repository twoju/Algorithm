n = int(input())
ans = n
for i in range(1, n + 1):
    num = sum(map(int, str(i)))

    if num + i == n:
        print(i)
        break
    if i == n:
        print(0)