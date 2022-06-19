def is_hansoo(n):
    
    
    
    
    if n < 100:
        return True
    
    
   


    new_n = list(str(n))
    new_n = list(map(int, new_n))
    

    if new_n[1] - new_n[0] == new_n[2] - new_n[1]:
        return True
    
    return False


      

N = int(input())

cnt = 0

i = 1
while i < N + 1:
    
    if is_hansoo(i):
        cnt += 1
    i += 1

print(cnt)