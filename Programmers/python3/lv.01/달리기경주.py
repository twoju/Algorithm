# Input
players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

# 1번 풀이
# while 문을 이용해서 이름 불린 순서에 따라 선수의 index 값을 찾아 앞 선수와 순서를 바꿔준다.

# def solution(players, callings):
#     call = len(callings)
#     i = 0
#     while i < call:
#         idx = players.index(callings[i])
#         players[idx], players[idx-1] = players[idx-1], players[idx]
#         i += 1
#     answer = players
#     return answer


# 2번 풀이
# for 문을 활용해서 순서와 이름을 담은 딕셔너리를 생성한 후, 이름 불린 선수와 앞선수를 바꿔준다.

# def solution(players, callings):
#
#     for call in callings:
#         player = {string: i for i, string in enumerate(players)}
#         pre, index = player[call] - 1, player[call]
#         players[pre], players[index] = players[index], players[pre]
#
#     answer = players
#     return answer


# 3번 풀이
# for 문을 활용하고, .index() 를 사용해서 앞 선수와 순서를 바꿔준다.
# 실행 시간이 가장 짧고, 가장 많은 테스트 케이스를 통과한 코드

# def solution(players, callings):
#     for i in range(len(callings)):
#         idx = players.index(callings[i])
#         players[idx], players[idx - 1] = players[idx - 1], players[idx]
#     answer = players
#     return answer


# 3번 해설
# 마찬가지로 16개 중에 5개가 시간 초과로 실패
# dict 형태로 변환하여 .index 를 사용하지 않았으나, 매번 players_list dict 를 다시 생성하는 점이
# 문제로 작용하는 것 같다.

# def solution(players, callings):
#     for i in callings:
#         players_list = {players[i]:i for i in range(len(players))}
#         index = players_list.get(i)
#         players[index], players[index - 1] = players[index - 1], players[index]
#     answer = players
#     return answer


# 합격 풀이
def solution(players, callings):
    players_list = {players[i]:i for i in range(len(players))}
    for i in callings:
        index = players_list.get(i)
        front_player = players[index - 1]
        players[index], players[index - 1] = players[index - 1], players[index]
        players_list[i] = index - 1
        players_list[front_player] = index

    answer = players
    return answer


print(solution(players, callings))

# 총평
# 16개 테스트 케이스 중에 5개가 시간 초과로 실패했다..
# 리스트 값을 계속 수정해서 오래 걸리는 것 이거나 이름 불리는 선수의 수가 많아져서 오래 걸리는 것 같음.
# 이름 불린 수를 카운트해서 현재 위치에서 빼주는 방법도 생각했으나,
# 숫자 값이 같은 경우 우위를 정하는 방법을 알 수 없었다.

# 총평 : 230825
# 다시 풀기까지 시간이 많이 지났다.. 프로젝트 하는 동안 알고리즘을 너무 등한시 했다..
# 파이썬을 까먹었나 했지만, 그래도 푸는 방법은 기억에 남아서 다행이다.
# dictionary 를 생성하는 형식이나, for 문 안에 최소의 변화만 주는 방법을 더 연습해야겠다.