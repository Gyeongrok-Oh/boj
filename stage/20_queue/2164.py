from collections import deque


N = int(input())
card_list = range(1, N+1)
card_list = deque(card_list)

while len(card_list) > 1:
    card_list.popleft()
    move_n = card_list.popleft()
    card_list.append(move_n)

print(card_list[0])