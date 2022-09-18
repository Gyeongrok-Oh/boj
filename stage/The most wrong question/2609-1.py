def gcd(x, y):
    if x < y:
        x, y = y, x

    i = y
    while i > 0:
        if x % i == 0 and y % i == 0:
            return i
        i -= 1
        

def lcm(x, y):
    if x < y:
        x, y = y, x

    i = x
    while i < x * y + 1:
        if i % y == 0:
            return i
        i += x


if __name__ == "__main__":
    x, y = map(int, input().split())

    print(gcd(x, y))
    print(lcm(x, y))