student = [False for _ in range(31)]

for _ in range(28):
    number = int(input())
    student[number] = True

for i in range(1, 31):
    if student[i] == False:
        print(i)