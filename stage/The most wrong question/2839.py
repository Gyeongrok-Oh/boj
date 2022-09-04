N = int(input())

if N < 5 and N != 3:
    print(-1)
    exit()

result = 0

while N % 5 != 0:
    if N < 0:
        result += -1
        print(result)
        exit()
    N -= 3
    result += 1

result += N // 5

print(result)