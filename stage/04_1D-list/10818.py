n = int(input())
a_list = list(map(int, input().split()))
print(min(a_list), max(a_list))



N = int(input())
integers = map(int, input().split())
min_integer = -1000000
max_integer = 1000000
i = 0
while i < N:
    if min_integer > integers[i]:
        min_integer == integers[i]
    elif max_integer < integers[i]:
        max_integer = integers[i]
    i += 1
print(max_integer, min_integer) 