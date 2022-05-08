word = input()

location_of_alphabets = [-1] *  26

i = 0
while i < len(word):
    location = ord(word[i]) - 97
    if location_of_alphabets[location] == -1:
        location_of_alphabets[location] = i
    i += 1

i = 0
while i < len(location_of_alphabets):
    print(location_of_alphabets[i], end=' ')
    i += 1