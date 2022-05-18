import sys

T = int(sys.stdin.readline().rstrip())

_ = 0
while _ < T:
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A + B)
    _ += 1