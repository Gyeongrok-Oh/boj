word = input().upper()

alphabet_counts = [0] * 26

i = 0
while i < len(word):
    alphabet_location = ord(word[i]) - 65
    alphabet_counts[alphabet_location] += 1
    i += 1

max_count = 0
max_count_count = 0

i = 0
while i < 26:
    count = alphabet_counts[i]
    if count > max_count:
        max_count = count
        max_count_index = i
        max_count_count = 1
    elif count == max_count:
        max_count_count += 1
    i += 1

if max_count_count == 1:
    print(chr(max_count_index + 65))
else:
    print('?')