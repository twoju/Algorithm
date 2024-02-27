while True:
    n = str(input().strip())
    if n == '0':
        break
    ans = 1 + len(n)
    for i in range(len(n)):
        if n[i] == '1':
            ans += 2
        elif n[i] == '0':
            ans += 4
        else:
            ans += 3
    print(ans)