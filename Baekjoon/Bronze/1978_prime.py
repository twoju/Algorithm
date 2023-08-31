import sys
sys.stdin = open('1978_prime.txt', 'r')

N = int(sys.stdin.readline())
input = [int(i) for i in sys.stdin.readline().split()]

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

cnt = 0
for i in range(N):
    if isPrime(input[i]) == True:
        cnt += 1
# if isPrime(i for i in range(N)) == True:
#     cnt += 1

# for i in range(N):
#     if input[i] != 1:
#         for j in range(2, int(input[i] ** 0.5) + 1):
#             if input[i] % j == 0:
#                 cnt -= 1
#     else:
#         cnt -= 1

print(cnt)
