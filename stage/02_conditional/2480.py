a_list = list(map(int, input().split()))

a_list.sort()

if a_list[0] == a_list[1] == a_list[2]:
    print(10000 + a_list[0]*1000)
elif a_list[0] ==  a_list[1] or  a_list[1] == a_list[2]:
    print(1000 + a_list[1]*100)
else:
    print(a_list[2]*100)  # teacher's coding
