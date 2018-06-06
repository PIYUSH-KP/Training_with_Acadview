class Stack:
    def __init__(self):
        self.stack = list()

    #Add elements to stack
    def push(self,data):
            self.stack.append(data)
            return True
        

    #Removing element from the stack(Last In First Out)
    def pop(self):
        if len(self.stack)<=0:
            return ("Stack Empty!")
        return self.stack.pop()
        
    def size(self):
        return len(self.stack)

myStack = Stack()
myStack.push(5)
print(myStack.stack)
print("Size of stack: " + str(myStack.size()))

myStack.push(6)
print(myStack.stack)
print("Size of stack: " + str(myStack.size()))

myStack.push(9)
print(myStack.stack)
print("Size of stack: " + str(myStack.size()))
myStack.push(3)
print(myStack.stack)
print("Size of stack: " + str(myStack.size()))

print("popped " + str(myStack.pop()))
print(myStack.stack)
print("Size of stack: " + str(myStack.size()))

print("popped " + str(myStack.pop()))
print(myStack.stack)
print("Size of stack: " + str(myStack.size()))

print("popped " + str(myStack.pop()))
print(myStack.stack)
print("Size of stack: " + str(myStack.size()))


