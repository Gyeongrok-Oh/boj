def gcd(a, b):
    while b > 0:
        a, b = b, a % b
        
    return a

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))


def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == "__main__":
    
    print(lcm(a, b))




# x, y = map(int, input(). split())

# if x < y :
#     x, y = y , x

# i = 1
# while i < y + 1:
#     if x % i == 0 and y % i == 0:
#         gcd = i
#     i += 1

# print(gcd)
# print(gcd * (x // gcd) * (y // gcd))