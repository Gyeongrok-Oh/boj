def is_dz(substring):
    return substring == "dz"

def is_croatia(substring):
    croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    return substring in croatia

string = input()

count = 0

i = 0
while i < len(string) - 1:
    substring = string[i:i+2]
    count += 1
    if is_dz(substring):
        if i + 2 < len(string) and string[i+2] == '=':
            i += 3
        else:
            i += 1
    elif is_croatia(substring):
        i += 2
    else:
        i += 1

if i == len(string) - 1:
    count += 1

print(count)