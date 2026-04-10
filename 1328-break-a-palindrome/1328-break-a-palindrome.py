class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        SIZE = len(palindrome)
        result = ""

        if SIZE == 1:
            return("")

        for i in range(SIZE // 2):
            if palindrome[i] == "a":
                result += "a"
            else:
                result += "a"
                # add all other characters 
                result += palindrome[i+1:]
                return(result)
        
        result = palindrome[:SIZE-1] + "b"
        print(result)
        return(result)
        
