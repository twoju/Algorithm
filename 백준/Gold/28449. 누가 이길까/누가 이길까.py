import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
hi = sorted(list(map(int, input().split())))
arc = sorted(list(map(int, input().split())))

total = n * m
h_win = 0
tie = 0

for i in hi:
    l, r = bisect_left(arc, i), bisect_right(arc, i)
    tie += r - l
    h_win += l

print(h_win, total - (h_win + tie), tie)