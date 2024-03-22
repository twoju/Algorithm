def solution(brown, yellow):
    ans = []
    tmp = [(1, yellow)]
    for i in range(2, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            tmp.append((i, yellow // i))
    for cur in tmp:
        x, y = cur[0], cur[1]
        if brown - (2 * x) == 2 * y + 4:
            ans = [y + 2, x + 2]
    return ans