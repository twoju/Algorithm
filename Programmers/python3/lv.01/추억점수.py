name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

def solution(name, yearning, photo):
    answer = []
    score = {name[i]: yearning[i] for i in range(len(name))}
    photo_score = 0
    for i in range(len(photo)):
        for j in photo[i]:
            if j in name:
                photo_score += score.get(j)
        answer.append(photo_score)
        photo_score = 0
    return answer

print(solution(name, yearning, photo))
# answer = [19, 15, 6]