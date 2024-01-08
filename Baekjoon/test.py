import sys
input = sys.stdin.readline

def test(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return 0
    return 1

n = int(input().strip())

if n == 1:
    print('no')
    sys.exit(0)

if not test(n):
    print('no')
    sys.exit(0)

new = ''

for i in str(n):
    ni = int(i)
    if ni == 6:
        new += '9'
    elif ni == 9:
        new += '6'
    else:
        new += str(ni)
    if ni in [3, 4, 7]:
        print('no')
        sys.exit(0)


new = new[::-1]
if new[0] == '0':
    print('no')
    sys.exit(0)

t = int(new)
if test(t):
    print('yes')
else:
    print('no')


# n, k = map(int, input().split())

# if n == k:
#     print('Impossible')
# elif n == k + 1:
#     for i in range(1, n + 1):
#         print(i, end=' ')
# else:
#     arr = [i for i in range(1, n + 1)]
#     cnt = n - 1
#     turn = 1
#     while True:
#         if cnt == k:
#             break
#         if turn >= n - 1:
#             break
#         if cnt % 2 == 1:
#             arr[0], arr[n - 1] = arr[n - 1], arr[0]
#             cnt -= 1
#         elif cnt % 2 == 0:
#             arr[turn], arr[turn + 1] = arr[turn + 1], arr[turn]
#             cnt -= 2
#             turn += 2

#     print(*arr)
