dice = [[1,2,3,4,5,6], [3,3,3,3,4,4], [1,3,3,4,4,4], [1,1,4,4,5,5]]

from itertools import product

def solution(dice):
    n = len(dice)
    total = 6 ** (n // 2)
    selected = []

    def select_dice(cur, arr):
        items = arr[:]
        if cur == n:
            if len(arr) == n // 2:
                selected.append(items)
            return
        items.append(cur)
        select_dice(cur + 1, items)
        select_dice(cur + 1, arr)
    
    select_dice(0, [])

    case = len(selected)

    win = [0 for _ in range(case)]

    for idx, now in enumerate(selected):
        A = [0 for _ in range(total)]
        B = [0 for _ in range(total)]
        b_dice = [i for i in range(n) if i not in now]

        a = list(product(*list(dice[i] for i in now)))
        b = list(product(*list(dice[i] for i in b_dice)))
        for i in range(total):
            A[i] += sum(a[i])
            B[i] += sum(b[i])

        A.sort()
        B.sort()

        for i in range(total):
            for j in range(total):
                if A[i] <= B[j]:
                    break
                win[idx] += 1

    return list(i + 1 for i in selected[win.index(max(win))])

print(solution(dice))