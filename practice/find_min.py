numbers = [9, 4, 5, 1, 7] # number < 10


min_value = 9

i = 0
while i < len(numbers):
    if min_value > numbers[i]:
        min_value = numbers[i]
    i += 1

print(min_value)


min_value = numbers[0]

i = 1
while i < len(numbers):
    if min_value > numbers[i]:
        min_value = numbers[i]
    i += 1

print(min_value)


min_index = 0

i = 1
while i < len(numbers):
    if numbers[min_index] > numbers[i]:
        min_index = i
    i += 1

print(numbers[min_index])