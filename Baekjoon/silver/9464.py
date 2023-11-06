import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    score = []
    for _ in range(2):
        score.append(list(map(int, input().split())))

    if n == 1:
        print(*max(score))
    else:
        score[0][1] += score[1][0]
        score[1][1] += score[0][0]

        for i in range(2, n):
            score[0][i] += max(score[1][i - 1], score[1][i - 2])
            score[1][i] += max(score[0][i - 1], score[0][i - 2])

        ans = max(score[0][n - 1], score[1][n - 1])
        print(ans)