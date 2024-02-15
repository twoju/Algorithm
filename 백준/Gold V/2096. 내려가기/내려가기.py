import sys
input = sys.stdin.readline

n = int(input().strip())
numbers = list(map(int, input().split()))

big, small = numbers, numbers

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    big = [a + max(big[0], big[1]), b + max(big), c + max(big[1], big[2])]
    small = [a + min(small[0], small[1]), b + min(small), c + min(small[1], small[2])]
        
print(max(big), min(small))