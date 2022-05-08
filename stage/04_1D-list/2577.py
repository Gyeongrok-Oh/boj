A = int(input())
B = int(input())
C = int(input())

multiple = A * B * C

counts = [0] * 10

while True:
    digit = multiple % 10
    counts[digit] += 1
    multiple //= 10
    if multiple == 0:
        break

i = 0
while i < len(counts):
    print(counts[i])
    i += 1




print('---------')

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))