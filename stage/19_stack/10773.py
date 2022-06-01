from collections import deque
K = int(input())
numbers = []
numbers = deque(numbers)

_ = 0
while _ < K:
    N = int(input())
    if N == 0:
        numbers.pop()
    else:
        numbers.append(N)

    _ += 1
sum = 0
i = 0
while i < len(numbers):
    sum += numbers[i]

    i += 1
print(sum)