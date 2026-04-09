class Solution:
    def reverseWords(self, s: str) -> str:
        wCount = 0
        wList = []
        word = ""

        for ch in s:
            if ch == " ":
                if word:
                    wList.append(word)
                    word = ""
            else:
                word += ch
        if word:
            wList.append(word)
        print(wList)

        # Now swap using two pointers
        left = 0
        right = len(wList) - 1

        while left < right:
            wList[left], wList[right] = wList[right], wList[left]
            left += 1
            right -= 1
        
        return(" ".join(wList))