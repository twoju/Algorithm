import sys

height = []
for _ in range(9):
    input = int(sys.stdin.readline().strip())
    height.append(input)

height = sorted(height)

one, two = 0, 0
# 전체의 합에서 두개를 빼서 100이 되는지 확인
total = sum(height)
for i in range(9):
    for j in range(i + 1, 9):
        if total - (height[i] + height[j]) == 100:
            one = height[i]
            two = height[j]

height.remove(one)
height.remove(two)
for i in range(7):
    print(height[i])