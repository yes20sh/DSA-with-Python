from math import*

class Dictionary:
    def __init__ (self, size):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size
    
    def put(self, key, value):
        hashPosition = self.hash_function(key)
        if self.slot[hashPosition] == None:
            self.slot[hashPosition] = key
            self.data[hashPosition] = value
        else:
            if self.slot[hashPosition] == key:
                self.data[hashPosition] = value
            else:
                rehashingPosition = self.rehashing_function(hashPosition)
                while self.slot[rehashingPosition] != None and self.slot[rehashingPosition] != key:
                    rehashingPosition = self.rehashing_function(hashPosition)
                if self.slot[rehashingPosition] == None:
                    self.slot[hashPosition] = key
                    self.data[hashPosition] = value
                else:
                    self.data[hashPosition] = value
    
    def __setitem__(self,key, value):
        self.put(key, value)

    def rehashing_function(self,oldHashPosition):
        return (oldHashPosition + 1) % self.size
    
    def quadratic_probing(self,oldHashPosition):
        return (oldHashPosition + sqrt(oldHashPosition)) % self.size

    def hash_function(self,key):
        return abs(hash(key)) % self.size
    
    def __getitem__(self, key):
        return self.get(key)
        
    def get(self, key):
        startPostion = self.hash_function(key)
        curPosition = startPostion
        while self.slot[curPosition] != None:
            if self.slot[curPosition] == key:
                return self.data[curPosition]
            curPosition = self.rehashing_function(curPosition)
            if self.slot[curPosition] == self.slot[startPostion]:
                return "Not Found"
        return "Not Found"
    
    def __str__(self):
        for i in range(len(self.slot)):
            if self.slot[i] != None:
                print(f"{self.slot[i]} : {self.data[i]}")
        return " "
            
    

def main():
    d1 = Dictionary(3)
    d1.put("python", 45)
    d1.put("java", 45)
    d1.put("php", 100)

    print(d1.slot)
    print(d1.data)

    # updating the value
    d1['python'] = 1000
    print("---------- After Updating ------------")
    print(d1.slot)
    print(d1.data)
    print(f"python value : {d1['python']}")

    print(d1)

    
if __name__ == "__main__":
    main()