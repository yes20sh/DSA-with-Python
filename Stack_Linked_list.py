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
    
    def clear(self):
        self.top = None
    
    def sizeof(self):
        return self.size
   
        
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
            result = str(curr.data) + " " +  result 
            curr = curr.next
        return result

    # -------------------------------------------------------------------------------------

    # Q - 1 reverse the string
    def reverse(self):
        temp_stack = StackLinkedList()
        result = " "
        while not self.epty():
            item = self.pop()
            temp_stack.push(item)
            result =   result + str(item) + " "
        self.top = temp_stack.top
        return result
            
            

    # Q - 2 Text editor

    def text_editor(self):
        redo = StackLinkedList()
        while True:
            option = input('''
                Welcome to Text editor!
                - Enter 1 for Undo
                - Enter 2 for Redo
                - Enter 3 for Exit
                Choose your option : ''')
            if option == '1':
                if not self.epty():
                    item = self.pop()
                    redo.push(item)
                    print(f"Undo {item} & current stack {self}")
                else:
                    print("Empty stack")
                
            elif option == '2':
                if redo.pop() is not None:
                    item = redo.pop()
                    self.push(item)
                    print(f"Undo {item} & current stack {self}")
                else:
                    print("No redo available")

            elif option == '3':
                break
            else : 
                print("Wrong Option")
0        

stk = StackLinkedList()

stk.push(3)
stk.push(8)
stk.push(5)
stk.push(9)
print(f"Stack is empty or not :  {stk.empty()} ")
print(f"The peak element in array : {stk.peak()}")
print(stk)
stk.pop()
print(f"Size of stack : {stk.sizeof()}")
print(stk)
stk.clear()

# q1
stk.push("O")
stk.push("L")
stk.push("L")
stk.push("E")
stk.push("H")
print(stk)
print(f" Reverse the stack string : {stk.reverse()}")

# Q2
stk.text_editor()
print(stk)


    
