N = int(input())

result = 1

i = N
while i >= 1:
    result *= i
    i -= 1

print(result)