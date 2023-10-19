def check(cur, arr):
    if len(arr) == 4:
        # 자음, 모음
        co, vo = 0, 0
        for i in arr:
            if i in need:
                vo += 1
            else:
                co += 1
        if co >= 2 and vo >= 1:
            print(*arr)
            return
        return
    new_arr = arr
    new_arr.append(alpha[cur])
    check(cur + 1, new_arr)
    new_arr.pop()
    check(cur + 1, arr)


l, c = map(int, input().split())
alpha = list(map(str, input().split()))

need = ['a', 'e', 'i', 'o', 'u']
check(0, [])