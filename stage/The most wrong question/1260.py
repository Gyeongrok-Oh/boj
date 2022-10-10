def dfs():
    visited = [False] * (V + 1)

    stack = [START]

    while stack:
        # 2) 꺼내고
        now = stack.pop()

        # 3) 방문체크
        if visited[now]:
            continue
        visited[now] = True
        print(now, end=' ')

        for next in graph[now][::-1]:
            # 1) 넣고
            stack.append(next)
    print()


def bfs():
    visited = [False] * (V + 1)

    visited[START] = True
    print(START, end=' ')
    queue = [START]

    while queue:
        # 2) 꺼내고
        now = queue.pop(0)

        for next in graph[now]:
            # 1) 방문체크 & 넣고
            if visited[next]:
                continue
            visited[next] = True
            print(next, end=' ')
            queue.append(next)
    print()


if __name__ == "__main__":
    V, E, START = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs()
    bfs()