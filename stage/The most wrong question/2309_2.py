from itertools import combinations

nine_dwars = [int(input()) for _ in range(0, 9)]


seven_dwarfs = list(combinations(nine_dwars, 7))

for i in range(len(seven_dwarfs)):

    if sum(seven_dwarfs[i]) == 100:

        for j in range(7):

            print(sorted(list(seven_dwarfs[i]))[j])
            
        break


        
    
    

  
        
    