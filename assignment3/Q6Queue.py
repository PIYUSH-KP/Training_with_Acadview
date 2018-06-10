class Queue:
  def __init__(self):
      self.queue = list()

  #Add elements to queue
  def enqueue(self,data):
          self.queue.insert(0,data) #insert element at begining
          return True
      

  #deleting element from queue (First In First Out)
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("Empty Queue")

  #Getting the size of the queue
  def size(self):
      return len(self.queue)


myQueue = Queue()
myQueue.enqueue(5)
print(myQueue.queue)
print("Current Size of Queue is: " + str(myQueue.size()))

myQueue.enqueue(6)
print(myQueue.queue)
print("Current Size of Queue is: " + str(myQueue.size()))

myQueue.enqueue(9)
print(myQueue.queue)
print("Current Size of Queue is: " + str(myQueue.size()))

myQueue.enqueue(3)
print(myQueue.queue)
print("Current Size of Queue is: " + str(myQueue.size()))

print("Dequeued : " + str(myQueue.dequeue()))
print(myQueue.queue)
print("Current Size of Queue is: " + str(myQueue.size()))

print("Dequeued : " + str(myQueue.dequeue()))
print(myQueue.queue)
print("Current Size of Queue is: " + str(myQueue.size()))