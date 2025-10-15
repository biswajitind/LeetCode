class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return(''.join(res))

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        print(s)
        i = 0
        nstr = ''
        res = []
        while i < len(s):
            if s[i] == '#':
                n = int(nstr)
                tmp = ''
                for j in range(i+1, i+n+1):
                    tmp += s[j]
                res.append(tmp)
                nstr = ''
                i += n
            else:
                nstr += s[i]
            i += 1
        return(res)
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))