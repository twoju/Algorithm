N, M = map(int, input().split())

A = [i for i in map(int, input().split())]
B = [i for i in map(int, input().split())]

arr = sorted(A + B)
print(*arr)