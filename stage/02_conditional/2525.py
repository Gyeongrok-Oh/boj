







A, B = map(int, input().split())
C = int(input())

B += C
A += B // 60
B %= 60

if A >= 24:
    A %= 24

print(A, B)        #teacher