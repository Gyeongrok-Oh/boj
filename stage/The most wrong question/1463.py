N = int(input())

cycle = 0

while N != 1:
    print(N)
    
    if N % 3 == 0:
        N /= 3
        
    elif N % 2 == 0:
        N /= 2
        
    else:
        N -= 1
    
    cycle += 1

print(cycle)




