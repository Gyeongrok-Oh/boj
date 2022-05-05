n = []
i = 1
while i < 10:
    n.append(int(input()))
    i += 1
print(max(n))
print(n.index(max(n))+ 1 )
