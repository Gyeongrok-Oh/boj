N = int(input())

cycle = 0

while N != 1:
    
    if N % 3 == 0:
        N = N / 3
        
    elif N % 2 == 0:
        N = N / 2
        
    else:
        N = N - 1
    
    cycle += 1

print(cycle)




