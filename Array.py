import ctypes

class MyArray:
    def __init__(self):
        self.size = 1
        self.n = 0
        # Creating the ctypes array with size of self.size
        self.arr = self.__make_array(self.size)
    
    # create 
    def __make_array(self, capacity):
        # Creates a ctypes array (static) of given capacity
        return (capacity * ctypes.py_object)()
    
    # resize
    def __resize(self,capacity):
        newArr = self.__make_array(capacity)
        self.size = capacity
        for i in range(self.n):
            newArr[i] = self.arr[i]
        self.arr = newArr

    # len
    def __len__(self):
        return self.n
    
    #append
    def append(self, value):
        if self.n == self.size:
            self.__resize(self.size*2)
        self.arr[self.n] = value
        self.n = self.n + 1
    
    # print 
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.arr[i]) + ','
        return '[' + result[:-1] + ']'
    
    # Index
    def __getitem__ (self, index):
        for i in range(self.n):
            if i == index:
                return self.arr[i]

        return "Index error!"

    # Find
    def __getitem__ (self, value):
        for i in range(self.n):
            if self.arr[i] == value:
                return i

        return "Value error!"

    # Delete (pop)
    def pop(self) :
        if self.n == 0:
            print ("Array is empty.")
        else:    
            print (self.arr[self.n-1])
            self.n = self.n - 1 
    
    # Clear
    def clear(self):
        self.n = 0
    
    # Insert
    def insert(self, pos, value):
        if self.n == self.size:
            self.__resize(self.size*2)
        new_aar = []
        for i in (self.n, pos, -1):
            self.arr[i] = self.arr[i-1]
        
        self.arr[pos] = value
        self.n =  self.n + 1
    
    # Delete
    def delete(self, pos):
        for i in range(pos, self.n-1):
            self.arr[i] = self.arr[i+1]
        
        self.n = self.n - 1
    
    # remove
    def remove(self, item):
        pos = self.__getitem__(item)
        if type(pos) == int:
            self.delete(pos)
        else:
            return pos

    # min
    def min(self):
        if self.n == 0:
            return None
        min_num = self.arr[0]
        for i in range(1,self.n):
             if min_num > self.arr[i]:
                min_num = self.arr[i]
        return min_num
    
    # Max
    def max(self):
        if self.n == 0:
            return None
        max_num = self.arr[0]
        for i in range(1,self.n):
             if max_num < self.arr[i]:
                max_num = self.arr[i]
        return max_num
    
    # sum
    def sum(self):
        result = 0
        for i in range(self.n):
            result = result + self.arr[i] 
        return result
    
    # merge
    def merge(self, other_arr):
        for value in other_arr:
            self.append(value) 

def array_main():
    lst = MyArray()
    print()
    lst.append(3)
    lst.append(5)
    lst.append(6)
    print(f"Length of array : {len(lst)}")
    print(f"All element in array {lst}")
    print(f"The index position of 5 is {lst[1]}")
    lst.pop()
    # lst.clear()
    print(f"Length of array : {len(lst)}")
    print(f"The element in array : {lst[5]}")
    lst.insert(1,2)
    lst.delete(1)
    lst.remove(3)
    lst.append(8)
    lst.append(2)
    lst.append(56)
    lst.append(3)
    print(f"Minimum number in array : {lst.min()}")
    print(f"Maximum number in array : {lst.max()}")
    print(f"Sum of number in array : {lst.sum()}")
    lst2 = MyArray()
    lst2.append(4)
    lst2.append(5)
    print(f"Merge the arry : {lst.merge(lst2)}")
    print(f"All element in array {lst}")
    
def list_main():
    print()
    lst = [2,4,5]
    lst.append(23)

if __name__ == "__main__":
    option = input('''
        1 . Enter (1) for MyArray
        2 . Enter (2) for MyList
        Choice :  ''')
    if option == "1":
        array_main()
    elif option == "2":
        list_main()
    else:
        print("Invalid")
        

