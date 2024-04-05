def solution(answers):
    answer = []
    pattern = [[], [1, 2, 3, 4, 5], 
               [2, 1, 2, 3, 2, 4, 2, 5], 
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    ans = {1: 0, 2: 0, 3: 0}
    for i in range(len(answers)):
        for man in range(1, 4):
            pi = i % len(pattern[man])
            if pattern[man][pi] == answers[i]:
                ans[man] += 1
    for j in range(1, 4):
        if ans[j] == max(ans.values()):
            answer.append(j)
    return answer