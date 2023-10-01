board = [list(map(int, input().split())) for _ in range(7)]
ball = int(input())

left = []

turn = 0
# turn 은 세로 줄이고, 한 줄씩 다 체크해보는 것
while True:
    if turn >= 7:
        break

    test = board[:]
    for i in range(1, 7):
        if test[i][turn]:
            # 숫자 있는거 바로 위에 공 넣기
            test[i - 1][turn] = ball
            # 같은 row에 있는 숫자 없애기 코드 실행
            for x in range(6, -1, -1):
                # 밑에줄부터 가로로 가장 길게 연속된 리스트 찾아서 슬라이싱 한다음에 그 중에 같은 숫자 있으면 없애기
                max_cnt = 0
                cnt = 0
                s, e = 0, 0
                for y in range(7):
                    if test[x][y] == 0:
                        if max_cnt < cnt:
                            max_cnt = cnt
                        # 가로 줄에서 max length 를 세고, 리스트 슬라이싱 해서 그 숫자가 있는지 어떻게 찾지ㅠ
                        cnt = 0
                    else:
                        e += 1
    turn += 1

print(min(left))