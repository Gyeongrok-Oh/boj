subway = []

total = 0
_ = 1
while _ < 5:
    get_off, get_on = map(int, input().split())
    total += get_on - get_off
    subway.append(total)
    _ += 1


print(max(subway))
    