def gcd(x, y):
    if x < y:
        x, y = y, x

    while y > 0:
        x, y = y, x % y
    return x
        

def lcm(x, y):
    return x * y // gcd(x, y)


if __name__ == "__main__":
    x, y = map(int, input().split())

    print(gcd(x, y))
    print(lcm(x, y))