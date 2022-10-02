def fibonacci(N):
    if memo[N] == -1: # 한 번도 연산한 적이 없으면
        memo[N] = fibonacci(N - 1) + fibonacci(N - 2)
    return memo[N]

N = int(input())

memo = [-1] * 21
memo[0] = 0
memo[1] = 1

print(fibonacci(N))