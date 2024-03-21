def solution(friends, gifts):
    answer = 0
    n = len(friends)
    m = len(gifts)
    name ={friends[i]: i for i in range(n)}

    gifted = [[0] * n for _ in range(n)]
    score = [0] * n
    for i in range(m):
        a, b = gifts[i].split()
        na = name[a]
        nb = name[b]
        gifted[na][nb] += 1
        score[na] += 1
        score[nb] -= 1
    
    ans = [0] * n
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if visited[i][j]:
                continue
            if gifted[i][j] > gifted[j][i]:
                ans[i] += 1
            elif gifted[i][j] == gifted[j][i]:
                if score[i] > score[j]:
                    ans[i] += 1
                if score[i] < score[j]:
                    ans[j] += 1
            else:
                ans[j] += 1
            visited[i][j] = 1
            visited[j][i] = 1
    
    return max(ans)