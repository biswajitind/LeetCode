class Solution:
    def reverseVowels(self, s: str) -> str:
        # two pointer 
        sList = [" "] * len(s)

        vSet = set(['a', 'e', 'i', 'o', 'u'])

        left, right = 0, len(s) - 1
        while left <= right:
            
            if ((s[left].lower() in vSet) and 
               (s[right].lower() in vSet)):
               # swap
               sList[left] = s[right]
               sList[right] = s[left]
               left += 1
               right -= 1
            else:
                if not s[left].lower() in vSet:
                    sList[left] = s[left]
                    left += 1
                
                if not s[right].lower() in vSet:
                    sList[right] = s[right]
                    right -= 1                
        return("".join(sList))