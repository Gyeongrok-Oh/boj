









n = int(input())

_ = 0
while _ < n:
    r, s = list(map(str, input().split()))
    r = int(r)
    
    
    
    i = 0
    while i < len(s):
        result = s[i]* r
        result.replace(' ','' )
        print(result,end=' ')
        print()
        i += 1
    
    _ += 1