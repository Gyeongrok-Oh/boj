x, y = map(int, input(). split())

if x < y :
    x, y = y , x

i = 1
while i < y + 1:
    if x % i == 0 and y % i == 0:
        gcd = i
    i += 1

print(gcd)
print(gcd * (x // gcd) * (y // gcd))