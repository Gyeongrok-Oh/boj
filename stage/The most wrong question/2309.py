from itertools import combinations


def find_seven_dwarfs(nine_dwarfs):
    dwarfs_list = list(combinations(nine_dwarfs, 7))
    
    i = 0
    while i < len(dwarfs_list):
        seven_dwarfs = dwarfs_list[i]
        sum_of_dwarfs = 0
        j = 0
        while j < len(seven_dwarfs):
            sum_of_dwarfs += seven_dwarfs[j]
            j += 1
        if sum_of_dwarfs == 100:
            return sorted(seven_dwarfs)
        i += 1


if __name__ == "__main__":
    nine_dwarfs = [int(input()) for _ in range(9)]
    
    seven_dwarfs = find_seven_dwarfs(nine_dwarfs)

    i = 0
    while i < 7:
        print(seven_dwarfs[i])
        i += 1