import sys
sys.stdin = open('2562_max.txt', 'r')

arr = [int(sys.stdin.readline().strip()) for _ in range(9)]
for index, num in enumerate(arr):
    if num == max(arr):
        print(num)
        print(index + 1)