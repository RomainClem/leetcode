class Node:
  def __init__(self, key, val): 
    self.key, self.val = key, val
    self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.left, self.right = Node(), Node()

    def get(self, key: int) -> int:
        node = self.cache.get(key, -1)        
        if node == -1: return -1
        
        node.next.prev = node.prev
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        return node.data

        
    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity:
            head = self.head.next
            self.head.next = head.next
            head.next.prev = self.head
            self.cache.pop(head.key)
            return

        node = None

        if self.head.data == None:
            node = Node(value, key, prev=self.head)
            self.head.next = node

        else:
            node = Node(value, key, prev=self.tail)
            self.tail.next = node
            
        self.tail = node       
        self.cache[key] = node            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)