N, A = map(int, input().split())

K = 0
ans = A
while ans <= N:
    K += N // ans
    ans *= A
    
print(K)