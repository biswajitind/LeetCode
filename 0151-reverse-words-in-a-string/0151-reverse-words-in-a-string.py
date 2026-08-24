class Solution:
    def reverseWords(self, s: str) -> str:
        # Iterate over the string from end to the beginning.
        # collect the words in a list
        words = []
        word = ''
        for i in range(len(s) -1, -1, -1):
            if s[i] == ' ':
                if word:
                    words.append(word)
                    word = ''
            else:
                word = s[i] + word
        
        if word:
            words.append(word)

        return(' '.join(words))
