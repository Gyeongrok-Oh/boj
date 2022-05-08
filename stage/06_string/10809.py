word = input()

location_of_alphabet = [-1] *  26

i = 0
while i < len(word):
    index = ord(word[i]) - 97
    if location_of_alphabet[index] == -1:
        location_of_alphabet[index] = i
    i += 1

i = 0
while i < len(location_of_alphabet):
    print(location_of_alphabet[i], end=' ')
    i += 1