from collections import deque
queue = deque([1,2,3,4])
print(queue)
queue.append("Piyush")
print(queue)
queue.append("Python")
print(queue)
print("Popped " + str(queue.popleft()))
print(queue)
print("Popped " + str(queue.popleft()))
print(queue)