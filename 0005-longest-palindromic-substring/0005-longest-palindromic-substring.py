class Solution:
    def longestPalindrome(self, s: str) -> str:
        word = ''

        for i in range(len(s)):
            inc = 0
            # checkig for odd Palindrome wjile i is the center
            while i-inc >= 0 and i+inc < len(s):
                if s[i-inc] == s[i+inc]:
                    if len(s[i-inc:i+inc+1]) > len(word):
                        word = s[i-inc:i+inc+1]
                else:
                    break
                inc += 1

            inc = 0
            # Checkig for Even Palindrome while i is the center left
            while i-inc >= 0 and i+1+inc < len(s):
                if s[i-inc] == s[i+1+inc]:
                    if len(s[i-inc:i+inc+2]) > len(word):
                        word = s[i-inc:i+inc+2]
                else:
                    break
                inc += 1


                

            
            
        return(word)


                

            
