N = int(input())
arr = []
for _ in range(N):
    word = input()
    if word not in arr:
        arr.append(word)

first = sorted(sorted(arr), key=len)

for i in range(len(first)):
    print(first[i])