memo = [-1] * (10**6 + 1)
memo[1] = 0

N = int(input())

i = 2
while i < N + 1:
    min_list = [memo[i - 1]]
    if n % 2 == 0:
        min_list[memo[i // 2]]
    if n % 3 == 0:
        min_list[memo[i // 3]]
    memo[i] = min(min_list) + 1
    i += 1

print(memo[N])