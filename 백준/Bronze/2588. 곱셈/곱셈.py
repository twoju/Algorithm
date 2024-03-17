import sys
input = sys.stdin.readline

a = int(input().strip())
b = int(input().strip())

c = a * int(str(b)[2])
d = a * int(str(b)[1])
e = a * int(str(b)[0])

f = c + (d * 10) + (e * 100)

print(c)
print(d)
print(e)
print(f)