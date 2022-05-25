n = int(input())
score_list = list(map(int, input().split()))
sum = 0
i = 0
while i < n:
    sum += (score_list[i] / max(score_list) * 100)  / n
    i += 1    
print(sum)



