ans = 0
    
def solution(numbers, target):
    global ans
    func(0, 0, numbers, target)
    return ans

def func(cur, tmp, number, target):
    global ans
    n = len(number)
    if cur == n:
        if tmp == target:
            ans += 1
        return
    func(cur + 1, tmp + number[cur], number, target)
    func(cur + 1, tmp - number[cur], number, target)
