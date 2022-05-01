N = int(input())

newNumber = N
cycle = 0

while True:
    secondNumber = (newNumber // 10 + newNumber % 10) % 10
    newNumber = (newNumber % 10) * 10 + secondNumber
    cycle += 1
    if newNumber == N:
        break

print(cycle)