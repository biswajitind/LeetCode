class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.indList = []

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return(False)
        self.hashMap[val] = len(self.indList)
        self.indList.append(val)
        return(True)

    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            ind = self.hashMap[val]
            lastVal = self.indList[-1]
            self.hashMap[lastVal] = ind

            # swap the values
            self.indList[ind], self.indList[-1] = self.indList[-1], self.indList[ind]
            self.indList.pop()
            del self.hashMap[val]


            return(True)

        return(False)
    
    def getRandom(self) -> int:
        if self.indList:
            return(random.choice(self.indList))
        else:
            return(None)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()