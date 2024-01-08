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