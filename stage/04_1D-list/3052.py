a_list = []

i = 0
while i < 10:
    n = int(input())
    a_list.append(n % 42)
    i += 1
a_list = set(a_list)
print(len(a_list))