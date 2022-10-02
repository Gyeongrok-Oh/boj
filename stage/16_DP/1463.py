memo = [-1] * (10**6 + 1)
memo[1] = 0

N = int(input())

i = 2
while i < N + 1:
    
    i += 1

print(memo[N])