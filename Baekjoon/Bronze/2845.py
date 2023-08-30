# import sys
# for input in sys.stdin.readline:
#     personNum, scale = map(int, input.split())
#     news = list(str(map(int, input.split()) - personNum * scale))
#     print(' '.join(news))

# import sys
# sys.stdin = open('2845.txt', 'r')
# input = sys.stdin.readline()
# for i in range(len(input)):
#     personNum, scale = input.split()
#     news = input.split()
#     print(personNum, scale, news)

import sys
sys.stdin = open('2845.txt', 'r')
n, p = map(int, sys.stdin.readline().split())
news = list(i - n * p for i in map(int, sys.stdin.readline().split()))

print(*news)

