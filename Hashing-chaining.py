class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, key, value):
        newNode = Node(key, value)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode

    def search(self, key):
        curr = self.head
        index = 0
        while curr is not None:
            if curr.key == key:
                return index  # Return the correct index
            index += 1
            curr = curr.next
        return -1  # Key not found

    def get_node_by_index(self, index):
        temp = self.head
        counter = 0
        while temp is not None:
            if counter == index:
                return temp
            temp = temp.next
            counter += 1
        return None

    def traverse(self):
        curr = self.head
        result = ""
        while curr is not None:
            result += str(curr.key) + " --> " + str(curr.value) + "   "
            curr = curr.next
        return result
    
    def size(self):
        curr = self.head
        counter = 0
        while curr is not None:
            curr = curr.next
            counter += 1
        return counter

    def remove(self, key):
        curr = self.head
        if self.head is None:
            return
        if self.head.key == key:
            self.head = self.head.next
            return
        while curr.next is not None:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


class Dictionary:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = self.make_array_ll(self.capacity)

    def make_array_ll(self, capacity):
        return [LinkedList() for _ in range(capacity)]

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def get_node_index(self, bucketIndex, key):
        return self.buckets[bucketIndex].search(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def put(self, key, value):
        bucketIndex = self.hash_function(key)
        nodeIndex = self.get_node_index(bucketIndex, key)

        if nodeIndex == -1:
            self.buckets[bucketIndex].add(key, value)
            self.size += 1 
            loadFactor = self.size / self.capacity
            if loadFactor > 2:
                self.rehash()
        else:
            node = self.buckets[bucketIndex].get_node_by_index(nodeIndex)
            if node:
                node.value = value
    
    def rehash(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.size = 0
        self.buckets = self.make_array_ll(self.capacity)

        for bucket in old_buckets:
            curr = bucket.head
            while curr is not None:
                self.put(curr.key, curr.value)
                curr = curr.next
    
    def __getitem__(self, key):
        return self.get(key)
    
    def get(self, key):
        bucketIndex = self.hash_function(key)
        nodeIndex = self.buckets[bucketIndex].search(key)
        if nodeIndex == -1:
            return None
        node = self.buckets[bucketIndex].get_node_by_index(nodeIndex)
        return node.value if node else None

    def __delitem__(self, key):
        bucketIndex = self.hash_function(key)
        self.buckets[bucketIndex].remove(key)
        self.size -= 1
    
    def __str__(self):
        result = []
        for index, bucket in enumerate(self.buckets):
            result.append(f"Array index {index}: {bucket.traverse()}")
        return "\n".join(result)


def dictionary_main():
    dl = Dictionary(2)
    dl.put('python', 56)
    print(f"python: {dl['python']}")
    dl.put('java', 126)
    dl.put('php', 456)
    dl.put('c++', 4588)
    dl.put('c', 4588)
    
    print(f"Size: {dl.size}")
    
    del dl['python']
    print(dl)

if __name__ == "__main__":
    dictionary_main()
