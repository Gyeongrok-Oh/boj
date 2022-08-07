def generate(n):
    result = n

    n_list = list(map(int, str(n)))

    i = 0
    while i < len(n_list):
        result += n_list[i]
        i += 1

    return result


def solution(n):
    for i in range(1, n):
        if generate(i) == n:
            return i
    return 0


N = int(input())

print(solution(N))