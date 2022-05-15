
c = int(input())
_ = 0
while _ < c:
    count = 0
    scores=list(map(int,input().split()))
    avg= (sum(scores)-scores[0]) /scores[0]
    _ += 1

    for i in scores[1:]: 
        if i>avg: 
            count += 1 
    result = count /scores[0]*100 
    print(f"{result:.3f}%")

        
    





             
    

    
    
     
