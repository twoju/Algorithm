"""
이분 탐색으로 할 수 있는 것
1. 정렬된 배열에서 특정 값이 존재하는지 체크

2. a b c 형태로 있는 경우 b 중에 가장 왼쪽 또는 오른쪽 인덱스 찾기
"""

n = int(input())
a = sorted(list(map(int, input())))
m = int(input())
b = sorted(list(map(int, input())))

for i in b:
    exist = False

    s = 0
    e = n - 1

    while s <= e:
        # 인덱스의 가운데 점을 찍었을 때
        mid = (s + e) // 2

        if a[mid] == i:
            exist = True
            break

        if a[mid] > i:
            # mid ~ e 까지는 절대 정답이 아니다
            e = mid - 1
        elif a[mid] < i:
             s = mid + 1

    if exist:
        print(1)
    else:
        print(0)


"""
매개변수 탐색 형태가 단조성을 띄면 이분 탐색
(o x 형태인 경우)

매개변수 탐색 + 이분 탐색 : 최대를 최소로 하는 경우, 최소를 최대로
"""

def ok(k):
    min = k
    for i in range(1, k + 1):
        min += min(min, k // i)
    return