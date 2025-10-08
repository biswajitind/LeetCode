class listNode:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = {}
        self.head = listNode(-1, -1)
        self.tail = listNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node

        node.prev = prev
        node.next = self.tail

        self.tail.prev = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return(-1)
        node = self.nodeMap[key]
        self._remove(node)
        self._add(node)
        return(node.val)

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            prev_node = self.nodeMap[key]
            self._remove(prev_node)
        new_node = listNode(key, value)
        self._add(new_node)
        self.nodeMap[key] = new_node

        if len(self.nodeMap) > self.capacity:
            node_to_delete = self.head.next
            self._remove(node_to_delete)
            del self.nodeMap[node_to_delete.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)