def d(n):
    generated = n
    while n > 0:
        generated += n % 10
        n //= 10
    return generated
    

self_numbers = [True] * 10001

i = 1
while i < 10001:
    generated = d(i)
    if generated < 10001:
        self_numbers[generated] = False
    i += 1

i = 1
while i < 10001:
    if self_numbers[i]:
        print(i)
    i += 1