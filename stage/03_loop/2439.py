N = int(input())

i = 1
while i < N + 1:
    
    _ = 0
    while _ < N - i:
        print(' ', end='')
        _ += 1
        
    _ = 0
    while _ < i:
        print('*', end='')
        _ += 1

    print()

    i += 1