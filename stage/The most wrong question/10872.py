N = int(input())


total = 1

i = N
while i > 1:

    if N == 1:
        break

    total *= i
    i -= 1

print(total)