n = int(input())

_ = 0
while _ < n:
    r, s = list(map(str, input().split()))
    r = int(r)
    
    

    for i in s:
        print(r*i, end='')
    print()
    _ += 1