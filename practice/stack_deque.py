from collections import deque

a_list = [3, 4, 5]
stack = deque(a_list)
print(stack)

stack = deque()
print(stack)

# stack push
stack.append(3)
print(stack)
stack.append(4)
print(stack)

# stack pop
print(stack.pop())
print(stack)

# stack peek
print(stack[-1])
print(stack)