from collections import deque
history = deque()

history.append("Google")
history.append("YouTube")

history.appendleft("Home")

print("Browser History:")
print(history)

history.pop()
 
history.popleft()

print("\nUpdated History:")
print(history)
