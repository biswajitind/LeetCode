class TimeMap:

    def __init__(self):
        # since we know that the timestamp is increasing, we can simply append the new 
        # values of a key into an attau of tuple.
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            valueList = self.data[key]
            for i in range(len(valueList) - 1, -1, -1):
                if valueList[i][0] <= timestamp:
                    return(valueList[i][1])
        return("")

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)