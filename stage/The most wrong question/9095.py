def addition(N):

    if N == 1:
        return 1

    if N == 2:
        return 2

    if N == 3:
        return 4

    return addition(N - 1) + addition(N - 2) + addition(N - 3)

if __name__ == "__main__":
    T = int(input())

    _ = 0
    while _ < T:
        print(addition(int(input())))


        _ += 1