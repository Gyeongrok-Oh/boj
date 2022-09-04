score = [int(input()) for _ in range(5)]

i = 0
while i < 5:
    if score[i] < 40:
        score[i] = 40
    i += 1

print(int(sum(score) / 5))