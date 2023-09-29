T = int(input())
for _ in range(T):
    string = list(input())

    ans = 0
    add = 1
    for i in range(len(string)):
        if string[i] == 'O':
            ans += add
            add += 1
        else:
            add = 1
    print(ans)