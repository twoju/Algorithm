n = int(input())
now = list(map(int, input().split()))
m = max(now)

new = []
for i in now:
    new.append(i/m*100)

print(sum(new)/n)