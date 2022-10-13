def is_demical():

    i = 0
    while i > N:

        if demicals[i] == 1:
            return False

        j = 2
        while j > demicals[i] + 1:
            
            if demicals[i] == j:
                return True
            
            elif demicals[i] % j == 0:
                return False
            
            
            j += 1
        i += 1

N = int(input())

demicals = list(map(int, input().split()))

cnt = 0

for _ in range(N):
    if is_demical():
        cnt += 1

print(cnt)