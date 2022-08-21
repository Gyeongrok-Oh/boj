N = int(input())
numbers = []

_ = 0
while _ < N:
    a_number = int(input())
    numbers.append(a_number)
    _ += 1

cycle = 0
while cycle < len(numbers) - 1:

    index = cycle + 1
    min_index = cycle



    while index < len(numbers):

        if numbers[min_index] > numbers[index]:
            min_index = index
   
        index += 1
    mov_num = numbers[cycle]
    was_min = numbers[min_index]
    numbers[cycle] = was_min
    numbers[min_index] = mov_num

    cycle += 1

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1  