class HitCounter:

    def __init__(self):
        self.counter = [[0,i+1] for i in range(300)]

    def hit(self, timestamp: int) -> None:
        idx = int((timestamp - 1)%300)
        if self.counter[idx][1] == timestamp:
            self.counter[idx][0] += 1
        else:
            self.counter[idx][0] = 1            
            self.counter[idx][1] = timestamp            
        
        
    def getHits(self, timestamp: int) -> int:
        cnt = 0
        for x in self.counter:
            c,t = x[0],x[1]
            if timestamp - t < 300:
                cnt += c
        return cnt






