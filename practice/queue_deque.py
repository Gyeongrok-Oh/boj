from collections import deque

a_list = [3, 4, 5]
queue = deque(a_list)
print(queue)

queue = deque()
print(queue)

# queue push
queue.append(3)
print(queue)
queue.append(4)
print(queue)

# queue pop
print(queue.popleft())
print(queue)

# queue peek
print(queue[0])
print(queue)