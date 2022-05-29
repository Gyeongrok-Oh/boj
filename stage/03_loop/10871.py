N, X = map(int, input().split())
integers = list(map(int, input().split()))

i = 0
while i < N:
    if integers[i] < X:
        print(integers[i], end=' ')
    i += 1
