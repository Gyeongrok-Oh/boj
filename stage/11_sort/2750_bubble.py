N = int(input())

numbers = []

_ = 0
while _ < N:
    a_number = int(input())
    numbers.append(a_number)
    _ += 1

cycle = 1
while cycle < len(numbers):

    index = cycle - 1
    change_index = cycle
    while change_index < len(numbers):

        if numbers[index] > numbers[change_index]:
            numbers[index] , numbers[change_index] = numbers[change_index], numbers[index]
            

        change_index += 1
    cycle += 1

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1











# N = int(input())

# numbers = []

# _ = 0
# while _ < N:
#     number = int(input())
#     numbers.append(number)
#     _ += 1

# cycle = 0
# while cycle < N - 1:
#     index = 0
#     while index < N - 1 - cycle:
#         if numbers[index] > numbers[index +  1]:
#             numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
#         index += 1
#     cycle += 1

# for number in numbers:
#     print(number)