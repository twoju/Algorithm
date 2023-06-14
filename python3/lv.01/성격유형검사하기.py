# input
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]


def solution(survey, choices):
    answer = ''
    # 설문 조사 결과 점수를 저장할 score
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    # 답변에 따른 점수 가중치
    point = {1: 3, 2: 2, 3: 1, 5: 1, 6: 2, 7: 3}

    # choices 의 숫자에 따라 answer에 더할 문자를 정한다.
    for idx, choice in enumerate(choices):
        if choice == 4:
            pass
        if choice < 4:
            score[survey[idx][0]] += point[choice]
        elif choice > 4:
            score[survey[idx][1]] += point[choice]

    # 점수가 더 큰 유형 또는 사전 순서상 앞에 있는 문자를 더해준다.
    if score['R'] >= score['T']:
        answer += 'R'
    else:
        answer += 'T'

    if score['C'] >= score['F']:
        answer += 'C'
    else:
        answer += 'F'

    if score['J'] >= score['M']:
        answer += 'J'
    else:
        answer += 'M'

    if score['A'] >= score['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer


print(solution(survey, choices))
