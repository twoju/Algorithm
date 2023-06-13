players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

    # i = 0
    # while i < call:
    #     idx = players.index(callings[i])
    #     players[idx], players[idx-1] = players[idx-1], players[idx]
    #     i += 1


# def solution(players, callings):
#     for i in range(len(callings)):
#         idx = players.index(callings[i])
#         players[idx], players[idx - 1] = players[idx - 1], players[idx]
#     answer = players
#     return answer


def solution(players, callings):

    idx = {}
    for i, name in enumerate(players):
        idx[name] = i

    print(idx)

    for call in callings:
        now = idx[call]
        # 이 이름보다 하나 앞에 있는 사람의 value 값이랑 이 이름의 value 값이랑 바꾸면 되는데..
        # idx[call], idx[now-1]

    print(idx)
    answer = idx
    return answer


print(solution(players, callings))