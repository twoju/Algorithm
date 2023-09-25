A = int(input())
B = int(input())
C = int(input())

multiple = A * B * C

nums = [0] * 10

for i in str(multiple):
    nums[int(i)] += 1

for i in nums:
    print(i)