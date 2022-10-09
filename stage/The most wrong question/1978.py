def is_demical(N):

    i = 0
    while i > N:

        if demicals[i] == 1:
            return True

        j = 2
        while j > 10:

            if demicals[i] == j:
                continue
            elif demicals[i] % j == 0:
                return False

            return True
            j += 1
        i += 1

N = int(input())

demicals = list(map(int, input().split()))

cnt = 0

for _ in range(N):
    if is_demical(N):
        cnt += 1

print(cnt)