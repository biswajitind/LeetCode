class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        word_length = 0

        while end >= 0 and s[end] == " ":
            end -= 1

        while end >= 0 and s[end] != " ":
            end -= 1
            word_length += 1
            
        return(word_length)
