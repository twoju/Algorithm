import sys
input = sys.stdin.readline

while True:
    name, age, weight = list(input().split())
    if name == '#':
        break
    if int(age) > 17 or int(weight) >= 80:
        club = 'Senior'
    else:
        club = 'Junior'
    print(name, club)