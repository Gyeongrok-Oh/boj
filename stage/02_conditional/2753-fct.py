def isLeap(year):
    if year % 4 == 0 and not year % 100 == 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

year = int(input())
if isLeap(year):
    print(1)
else:
    print(0)