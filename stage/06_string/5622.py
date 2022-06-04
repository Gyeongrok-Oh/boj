cell = list(input().split())
sum = 0
print(cell)
i = 0
while i < len(cell):
    if cell[i] in ['A','B','C']:
        sum += 3
    elif cell[i] in ['D','E','F']:
        sum += 3
    i += 1
print(sum)

