from collections import deque

def interleave_queue(queue: deque):
    half_size = len(queue) // 2
    first_half = deque()

    for _ in range (half_size):
        first_half.append(queue.popleft())
    
    while first_half:
        queue.append(first_half.popleft())
        if queue:
            queue.append(queue.popleft())
            
    if half_size % 2 == 1:
        queue.append(queue.popleft())

    return queue

queue = deque()
for i in range(1,8):
    queue.append(i)

print(interleave_queue(queue))
