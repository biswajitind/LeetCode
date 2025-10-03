class WordDistance(object):

    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        self.wordsDict = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] in self.wordsDict:
                self.wordsDict[wordsDict[i]].append(i)
            else:
                self.wordsDict[wordsDict[i]] = [i]
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        locs_word1 = self.wordsDict[word1]
        locs_word2 = self.wordsDict[word2]

        dist = 50000

        for i in locs_word1:
            for j in locs_word2:
                if abs(i - j) < dist:
                    dist = abs(i - j)

                # if we already found. pair with distence 1
                # no need to check further. 
                if dist == 1:
                    return(dist)
        return(dist)



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)