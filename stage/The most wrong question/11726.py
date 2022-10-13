N = int(input())

dp = [- 1] * (N + 1)

if N < 3:
    print(N)

else: 

    dp[1] = 1
    dp[2] = 2

    for i in range(3, N + 1):

        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[i] % 10007)