class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        result = ""

        for ch in s:
            if ch == " ":
                if word:
                    if result:
                        result = word + " " + result
                    else:
                        result = word
                    word = ""
            else:
                word += ch
        if word:
            if result:
                result = word + " " + result
            else:
                result = word
        
        return(result)