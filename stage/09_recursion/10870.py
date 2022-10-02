N = int(input())

Fibonacci_n = [0, 1]



i = 2
while i < N + 1:
    Fibonacci_n.append(Fibonacci_n[i - 1] + Fibonacci_n[i - 2])
    i += 1
print(Fibonacci_n[N])

