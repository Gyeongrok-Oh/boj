def mutliple_3_or_another(num1, num2=3):
    return num1 * num2

print(mutliple_3_or_another(6, 7))
print(mutliple_3_or_another(6))

def multiple_3_4_or_other(num1, num2=3, num3=4):
    return num1 * num2 * num3

print(multiple_3_4_or_other(6, 7, 8))
print(multiple_3_4_or_other(6))
print(multiple_3_4_or_other(6, num3=8))