class ListNode:
    def __init__(self, key = -1, value = -1, next = None):
        self.key = key
        self.val = value
        self.next = next
    def add(self, key, value):
        cur = self
        while cur.next != None:
            if cur.next.key == key:
                # Lets update this node
                cur.next.val = value
                return()
            cur = cur.next
        cur.next = ListNode(key, value)

    def remove(self, key):
        cur = self
        while cur.next != None:
            if cur.next.key == key:
                # Lets remove this node
                cur.next = cur.next.next
                return()
            cur = cur.next
    def get(self, key):
        cur = self
        while cur.next != None:
            if cur.next.key == key:
                return(cur.next.val)
            cur = cur.next
        return(-1)

class MyHashMap:
    def __init__(self):
        self.data = [ListNode() for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % 1000
        self.data[hash_key].add(key, value)

    def get(self, key: int) -> int:
        hash_key = key % 1000
        return(self.data[hash_key].get(key))
        
    def remove(self, key: int) -> None:
        hash_key = key % 1000
        return(self.data[hash_key].remove(key))
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)