import sys
input = sys.stdin.readline

total_score = 0
ans = 0

as_grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

for _ in range(20):
    subject, score, grade = input().split()
    score = float(score)
    if grade != 'P':
        ans += score * as_grade[grade]
        total_score += score

print(ans / total_score)