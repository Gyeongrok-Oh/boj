N = int(input())

numbers = []

_ = 0
while _ < N:
    number = int(input())
    numbers.append(number)
    _ += 1

cycle = 0
while cycle < N - 1:
    index = 0
    while index < N - 1 - cycle:
        if numbers[index] > numbers[index +  1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
        index += 1
    cycle += 1

for number in numbers:
    print(number)