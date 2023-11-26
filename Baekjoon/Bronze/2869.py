a, b, v = map(int, input().split())

go = v - b
day = a - b

if go % day == 0:
    print(go // day)
else:
    print(go // day + 1)