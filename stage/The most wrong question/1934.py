def gcd(a, b):
    while b > 0:
        a, b = b, a % b
        
    return a

if __name__ == "__main__":

    T = int(input())
    _= 0
    while _< T:
        a, b = map(int, input().split())
        print(a * b // gcd(a, b))

        _ += 1
