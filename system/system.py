from collections import OrderedDict

class LRUCache:
    """
    https://leetcode.com/problems/lru-cache/
    Runtime: 192 ms, faster than 93.71% of Python3 online submissions for LRU Cache.
    Memory Usage: 21.8 MB, less than 42.42% of Python3 online submissions for LRU Cache.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._lru = OrderedDict()
        self._n = 0

    def get(self, key: int) -> int:
        if key in self._lru:
            value = self._lru.pop(key)
            self._lru[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._lru:
            self._lru.pop(key)
            self._n -= 1
        # if len(self._lru) >= self.capacity:
        if self._n >= self.capacity:
            self._lru.popitem(last=False)
            self._n -= 1
        self._lru[key] = value
        self._n += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)