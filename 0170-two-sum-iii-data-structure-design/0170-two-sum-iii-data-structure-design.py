class TwoSum:

    def __init__(self):
        self.values = []
        self.targets = set()
        

    def add(self, number: int) -> None:
        for val in self.values:
            s = val + number
            self.targets.add(s)

        self.values.append(number)

    def find(self, value: int) -> bool:
        if value in self.targets:
            return(True)
        return(False)
        
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)