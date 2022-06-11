N = int(input())

_ = 0
while _ < N:
    R, S = list(map(str, input().split()))
    R = int(R)

    i = 0
    while i < len(S):

        result = R * S[i]
        
        print(result, end='')
        
        i += 1
    print()
    _ += 1