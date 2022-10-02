import sys
sys.setrecursionlimit(10**6)

def generate_one(n):
    if n == 1:
        return 0
    root = [generate_one(n - 1)]
    if n % 3 == 0:
        root.append(generate_one(n // 3))
    if n % 2 == 0:
        root.append(generate_one(n // 2))
    return min(root) + 1

N = int(input())
print(generate_one(N))