l = int(input())
word = list(input())

ans = 0

for i in range(l):
    ans += (ord(word[i]) - 96) * (31 ** i)

print(ans % 1234567891)