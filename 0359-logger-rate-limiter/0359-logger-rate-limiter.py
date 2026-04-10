class Logger:

    def __init__(self):
        self.hMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        #print(self.hMap)
    
        if message in self.hMap:
            mTime = self.hMap[message]
            if timestamp >= mTime:
                self.hMap[message] = timestamp + 10
                return(True)
            else:
                return(False)
        else:
            self.hMap[message] = timestamp + 10
            return(True)


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)