# cur = 0~4 요일, score 학점 ==k, last 이전 교시 끝난 시간
def bfs(cur, score, last):
    global cnt
    if score > k:
        return
    if score == k:
        cnt += 1
        return
    if cur == 4:
        return
    for i in range(cur, n):
        if last != -1 and timetable


n, k = map(int, input().split())
timetable = [[] for _ in range(5)]
for _ in range(n):
    w, s, e = map(int, input().split())
    timetable[w - 1].append([s - 1, e - 1])

for i in range(5):
    timetable[i].sort()

cnt = 0

bfs(0, 0, -1)

print(cnt)