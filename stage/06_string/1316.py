


def is_group_word(word):
    is_appeared_list = [False] * 26
    word = '_' + word

    i = 1
    while i < len(word):
        location = ord(word[i]) - 97
        if word[i] == word[i - 1]:
            pass
        elif not is_appeared_list[location]:
            is_appeared_list[location] = True
        else:
            return False
        i += 1

    return True


if __name__ == "__main__":
    N = int(input())

    group_word_count = 0

    _ = 0
    while _ < N:
        word = input()
        if is_group_word(word):
            group_word_count += 1

        _ += 1

    print(group_word_count)