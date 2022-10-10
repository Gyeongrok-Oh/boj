if __name__ == "__main__":
    N = int(input())

    memo = [[0, 0], [0, 0]]

    for _ in range(N):
        score = int(input())
        memo.append([memo[-1][1] + score, max(memo[-2]) + score])
    
    print(max(memo[-1]))