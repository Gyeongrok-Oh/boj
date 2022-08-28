from itertools import permutations, combinations

print(list(permutations([1, 2, 3], 2)))

print(list(combinations([1, 2, 3], 2)))

input_list = list(range(1, 10))
print(len(list(combinations(input_list, 7))))
for x in list(combinations(input_list, 7)):
    print(x)