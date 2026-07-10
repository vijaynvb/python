from collections import deque

queue = deque()
 
queue.append("Customer 1")
queue.append("Customer 2")
queue.append("Customer 3")
 
print("First Customer:", queue[0])
 
print("Queue Size:", len(queue))
 
print("Served:", queue.popleft())

print("Current Queue:", list(queue))