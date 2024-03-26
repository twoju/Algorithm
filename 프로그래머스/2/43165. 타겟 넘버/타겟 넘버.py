ans = 0
    
def solution(numbers, target):
    global ans
    n = len(numbers)
    func(0, 0, n, numbers, target)
    return ans

def func(cur, tmp, n, number, target):
    global ans
    if cur == n:
        if tmp == target:
            ans += 1
        return
    func(cur + 1, tmp + number[cur], n, number, target)
    func(cur + 1, tmp - number[cur], n, number, target)
