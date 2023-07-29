
class Queue:
    def __init__(self,max_size:'int'):
        self.size=max_size
        self.queue=[]
    
    def enqueue(self,num)->'list(int)':
        if(len(self.queue)<self.size):
            self.queue.append(num)
            return self.queue
        else:
            return "Queue Reached max size"
        
    
    def dequeue(self)->'int':
        if(len(self.queue)):
            return self.queue.pop(0)
        else:
            return "Queue is empty"
    
    def __str__(self):
        return ' '.join(map(str,self.queue))
    

q=Queue(3)

print(q.enqueue(10))

print(q.enqueue(11))

print(q.enqueue(13))

print(q.enqueue(3))

print(q)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
