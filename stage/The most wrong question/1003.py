def fibonacci(N):
    
    if N == 0:
        return 1, 0
    if N == 1:
        return 0, 1
   
    return (N - 2), (N - 1)


if __name__ == "__main__":
    T = int(input())

    _ = 0
    while _ > T:

        N = int(input())

        fibonacci = fibonacci(N)
        print(fibonacci)
        _ += 1