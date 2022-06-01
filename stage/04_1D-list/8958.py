n = int(input())

_ = 0
while _ < n:
    sum = 0
    score = 0
    quiz_result = input()\
    i = 0
    while i < len(quiz_result):
        
        if quiz_result[i] == 'O':
            score += 1
            sum += score
            
        elif quiz_result[i] == 'X':
            score = 0
        i +=1
    _ +=1
        
    print(sum)

