n = int(input()) 
a_list = list(input()) 

sum = 0

i = 0
while i < len(a_list):
    sum += int(a_list[i])
    i += 1

print(sum)