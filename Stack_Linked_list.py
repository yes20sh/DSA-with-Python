class Node:
    def __init__(self, value):
        self.next = None
        self.data = value

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def epty(self):
        if self.top == None:
            return 1
        else: 
            return 0

    def empty (self):
        if  self.epty():
            return "Empty"
        else:
            return "Not Empty"
        
    def peak(self):
        if self.epty():
            return "No Element"
        return self.top.data

    def push(self, value):
        newNode = Node(value)
        if self.top == None:
            self.top = newNode 
            return
        newNode.next = self.top
        self.top = newNode
        self.size += 1
    
    def pop(self):
        if self.epty():
            return "No Element"
        curr = self.top
        self.top = self.top.next
        return curr.data


    def __str__(self):
        if self.epty():
            return "No Element"
        curr = self.top
        result = " "
        while curr != None:
            result = result + str(curr.data) + " -> "
            curr = curr.next
        return result[:-3]

stk = StackLinkedList()

stk.push(3)
stk.push(8)
stk.push(5)
stk.push(9)
print(f"Stack is empty or not :  {stk.empty()} ")
print(f"The peak element in array : {stk.peak()}")
print(stk)
stk.pop()
print(stk)


    
