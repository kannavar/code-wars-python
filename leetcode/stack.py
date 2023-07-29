class Stack:
    def __init__(self,num):
        self.stack=[num]

    def push(self,num):
        self.stack.append(num)
        return self.stack
    
    def pop(self):
        if len(self.stack):
            return self.stack.pop()
        else:
            return "Stack is Empty"
    
    def display(self):
        print(self.stack)
    


s=Stack(2)
print(s.push(3))
print(s.push(4))
print(s.push(5))
print(s.pop())
s.display()

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
