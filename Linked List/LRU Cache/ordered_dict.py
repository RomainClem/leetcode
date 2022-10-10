from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.cap:
            # first_key = next(iter(self.cache))
            # self.cache.pop(first_key)
            self.cache.popitem(last = False)
        
        self.cache[key] = value