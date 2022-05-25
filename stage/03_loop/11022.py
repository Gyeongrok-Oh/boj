T = int(input())
i = 1
while i < T + 1:
    A, B = map(int, input().split())
    print("Case #{0}: {1} + {2} = {3}".format(i, A, B, A + B))
    i += 1