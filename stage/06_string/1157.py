word = input().upper()

alphabet_counts = [0] * 26

i = 0
while i < len(word):
    alphabet_location = ord(word[i]) - 65
    alphabet_counts[alphabet_location] += 1
    i += 1

i = 0
max_count = 0
while i < 26:
    count = alphabet_counts[i]
    if count > max_count:
        max_count = count
    i += 1

i = 0
max_count_count = 0
while i < 26:
    count = alphabet_counts[i]
    if count == max_count:
        max_count_count += 1
    i += 1

if max_count_count == 1:
    i = 0
    while i < 26:
        count = alphabet_counts[i]
        if count == max_count:
            max_index = i
        i += 1
    print(chr(max_index + 65))
else:
    print('?')