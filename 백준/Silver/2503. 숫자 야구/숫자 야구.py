import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input().strip())
qna = [list(map(int, input().split())) for _ in range(n)]

guess = 0
nums = list(permutations(range(1, 10), 3))
ans = [True] * len(nums)
for q in qna:
    num = str(q[0])
    s = q[1]
    b = q[2]

    for c in range(len(nums)):
        cur = nums[c]
        strike = 0
        ball = 0
        for i in range(3):
            if int(num[i]) in cur:
                if i == cur.index(int(num[i])):
                    strike += 1
                else:
                    ball += 1
        if strike != s or ball != b:
            ans[c] = False

print(sum(ans))