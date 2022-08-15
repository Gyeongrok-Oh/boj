N = int(input())

numbers = []

_ = 0
while _ < N:
    number = int(input())
    numbers.append(number)
    _ += 1

cycle = 1
while cycle < N:
    key = numbers[cycle]
    index = cycle - 1
    while index > -1:
        if numbers[index] > key:
            numbers[index + 1] = numbers[index]
        else:
            break
        index -= 1
    numbers[index + 1] = key
    cycle += 1

for number in numbers:
    print(number)