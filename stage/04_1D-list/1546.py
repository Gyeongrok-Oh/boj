n = int(input())
score_list = list(map(int, input().split()))
sum = 0

for total in score_list:
    sum += (total / max(score_list) * 100)  / n
    
print(sum)



