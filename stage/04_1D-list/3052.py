a_list = []

_ = 0
while _ < 10:
    n = int(input())
    a_list.append(n % 42)
    _ += 1
a_set = set(a_list)
print(len(a_set))