def recur(f, s):
    pass


able = list(map(int, input().split()))

for _ in range(5):
    first, second = map(int, input().split())
    print(recur(first, second))