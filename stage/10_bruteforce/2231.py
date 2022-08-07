def generate(n):
    result = n

    n_list = list(map(int, str(n)))

    i = 0
    while i < len(n_list):
        result += n_list[i]
        i += 1

    return result


N = int(input())

isExist = False

for i in range(1, N):
    if generate(i) == N:
        print(i)
        isExist = True
        break

if not isExist:
    print(0)