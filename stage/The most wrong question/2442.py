N = int(input())

i = 1
while i < N + 1:

    print(' ' * (N - i ), end ='')
    print('*' * (2 * i - 1))
    i += 1