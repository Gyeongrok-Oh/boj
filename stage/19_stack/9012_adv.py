from collections import deque

def is_vps(ps):
    stack = deque()

    i = 0
    while i < len(ps):
        
        if ps[i] == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False

        i += 1

    if stack:
        return False
    else:
        return True

if __name__ == "__main__":
    T = int(input())

    _ = 0
    while _ < T:
        ps = input()

        if is_vps(ps):
            print("YES")
        else:
            print("NO")

        _ += 1