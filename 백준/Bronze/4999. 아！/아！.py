import sys
input = sys.stdin.readline

speak = list(input().strip())
hear = list(input().strip())

if len(speak) < len(hear):
    print('no')
else:
    print('go')