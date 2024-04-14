class QueueusingStacks:
    def __init__(self):
        self.stack_enqueue=[]
        self.stack_dequeue=[]
    def enqueue(self,item):
        self.stack_enqueue.append(item)
    def dequeue(self):
        if not self.stack_dequeue:
            return "queue is empty"
        else:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()
    def peek(self):
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                return "queue is empty"
            else:
                while self.stack_enqueue:
                    self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue[-1]
    def is_empty(self):
        return not self.stack_/enqueue and not self.stack_dequeue
queue=QueueusingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())







        
                
