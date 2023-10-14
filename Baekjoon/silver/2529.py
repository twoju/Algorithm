def find(cur, pre):
    global res, max_num, min_num
    if cur == k:
        now = ''
        for i in res:
            now += str(i)
        max_num = max(max_num, now)
        min_num = min(min_num, now)
        return
    if arr[cur] == '<':
        for i in range(pre + 1, 10):
            if selected[i]:
                continue
            res[cur + 1] = i
            selected[i] = True
            find(cur + 1, i)
            selected[i] = False
    else:
        for i in range(pre):
            if selected[i]:
                continue
            res[cur + 1] = i
            selected[i] = True
            find(cur + 1, i)
            selected[i] = False


k = int(input())
arr = input().split()

selected = [False] * 10
max_num = '0'
min_num = '9876543210'

for i in range(10):
    res = [0] * (k + 1)
    res[0] = i
    selected[i] = True
    find(0, i)
    selected[i] = False

print(max_num)
print(min_num)