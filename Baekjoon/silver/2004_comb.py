N, M = map(int, input().split())

# n C m 의 끝자리 0의 개수를 구하라?
def isZero(C, num):
    cnt = 0
    divNum = num
    while C >= divNum:
        cnt += C // divNum
        divNum *= num
    return cnt

five = isZero(N, 5) - isZero(M, 5) - isZero(N - M, 5)
two = isZero(N, 2) - isZero(M, 2) - isZero(N - M, 2)

print(min(five, two))