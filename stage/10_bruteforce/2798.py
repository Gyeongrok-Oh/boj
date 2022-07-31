N, M = map(int, input().split())
card_list = list(map(int, input().split()))

result = 0

i = 0
while i < N - 2:
    j = i + 1
    while j < N - 1:
        k = j + 1
        while k < N:
            sum_of_cards = card_list[i] + card_list[j] + card_list[k]
            if sum_of_cards <= M: # 카드의 합이 M보다 크지 않을 때
                if sum_of_cards > result: # 그 전에 나왔던 최댓값보다 현재 카드의 합이 더 큰 숫자라면
                    result = sum_of_cards # 갱신
            k += 1
        j += 1
    i += 1

print(result)