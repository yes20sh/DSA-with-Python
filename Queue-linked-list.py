class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class QueueLinkedList:
    def __init__ (self):
        self.front = None
        self.rear = self.front
        self.size = 0
    
    def is_empty(self):
        return self.front == None
    
    # Enqueue 
    def enqueue(self, item):
        newNode = Node(item)
        if self.rear == None:
            self.front = newNode
            self.rear = self.front
            self.size += 1
        else:
            self.rear.next = newNode
            self.rear = newNode
            self.size += 1

    
    # Dequeue
    def dequeue(self):
       if self.front == None:
           print("Empty Queue")
           return
       else:
           self.front = self.front.next
           self.size -= 1
           return
        
    def __str__(self):
        curr = self.front
        result = " "
        while curr != None:
            result = result + str(curr.data) + " "
            curr = curr.next
        return result
    
    def front_item(self):
        return self.front.data

    def rear_item(self):
        return self.rear.data

qll = QueueLinkedList()
qll.enqueue(34)
qll.enqueue(56)
qll.enqueue(45)
print(qll)
qll.dequeue()
qll.enqueue(45)
qll.enqueue(76)
qll.enqueue(16)

print(qll)
print(f"size of queue : {qll.size}")
print(f"Queue is empty or not : {qll.is_empty()}")
print(f"Front item element : {qll.front_item()}")
print(f"Rear item element : {qll.rear_item()}")








        
