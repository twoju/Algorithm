N = int(input())

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if N == 1:
    pass
else:
    left = N
    for i in range(2, int(N ** 0.5) + 1):
        if isPrime(i) == True:
            while left % i == 0:
                print(i)
                left = left // i
    if left != 1:
        print(left)
                
        

# 정수 N이 주어질 때 소인수분해 하라
# 1. 소수(작은 수부터)로 정수 N을 나눠서 N이 1이 될 때까지 반복
# 2. 더이상 나눠지지 않는데 N이 1이 아니면 그 남은 수 출력
# 3. 정수 N이면 2부터 루트N + 1 범위 안에서 소수를 찾아서 나눠보면 된다
# 4. 소수를 찾는 방법은? 