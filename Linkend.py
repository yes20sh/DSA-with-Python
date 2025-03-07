class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
    
    def __len__(self):
        return self.n
    
    # Insertion ---------------------------------------------------------------------------

    # Insert from head
    def insert_head(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.n += 1
    
    # Insert from tail
    def append(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.n += 1
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newNode
            self.n += 1
    
    # insert in middle
    def insert_middle(self, value, after):
        newNode = Node(value)
        if self.head is None:
            print ("Empty")
            return
        curr = self.head
        while curr is not None:
            if curr.data == after:
                newNode.next = curr.next
                curr.next = newNode
                self.n += 1
                return
            curr = curr.next    
        print("Invalid value")      

    # Traverse ---------------------------------------------------------------------------

    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            result = result + str(curr.data) + " -> "
            curr = curr.next
        return result[:-3]

    # Deletion ---------------------------------------------------------------------------
    
    def delete_head(self):
        if self.head is None:
            print("Empty Linked List")
            return
        self.head = self.head.next
        self.n -= 1
    
    def clear(self):
        self.head = None
        self.n = 0

    def pop(self):
        curr = self.head
        if self.head is None:
            print("Empty Linked List")
            return
        elif curr.next == None:
            self.delete_head()
            return
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        self.n -= 1
    
    def remove(self, value):
        curr = self.head
        if self.head is None:
            print("Empty Linked List")
            return
        if self.head.data == value:
            delete_head()
            self.n -= 1
            return

        while curr.next != None:
            if curr.next.data == value:
                curr.next = curr.next.next
                self.n -= 1
                return 
            curr = curr.next      
        print("Invalid value")

    # search ---------------------------------------------------------------------------

    def search (self, value):
        curr = self.head
        index  = 0
        if self.head == None:
            print("List is Empty")
            return
        while curr is not None:
            if curr.data == value:
                index += 1
                return index
            index += 1
            curr = curr.next
        print("Not found")


ll = LinkedList()

ll.insert_head(12)
ll.insert_head(23)
ll.append(25)
ll.insert_middle(45,25)
ll.delete_head()
ll.pop()
ll.append(45)
ll.append(65)
ll.append(85)
ll.append(95)
ll.remove(45)

print(f"searching 65 : {ll.search(65)}")


print(ll)
print(f"Length of linked list : {len(ll)}")
ll.clear()