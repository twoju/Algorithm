arr = [False] + [True] * 10001

def d(n):
    num = n
    for i in str(n):
        num += int(i)
    if num < 10001:
        if arr[num]:
            arr[num] = False

for i in range(1, 10001):
    d(i)

for j in range(1, 10001):
    if arr[j] == True:
        print(j)