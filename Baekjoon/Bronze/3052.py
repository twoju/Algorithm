remain = []
for _ in range(10):
    n = int(input())
    if n % 42 not in remain:
        remain.append(n % 42)
print(len(remain))