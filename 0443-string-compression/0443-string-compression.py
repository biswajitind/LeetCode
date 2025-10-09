class Solution:
    def compress(self, chars: List[str]) -> int:

        r = 0
        w = 0
        while r < len(chars):
            group = 1
            while (r + group) < len(chars) and chars[r] == chars[r + group]:
                group += 1

            chars[w] = chars[r]
            w += 1         
            # Now its time to write the number of repeats 
            if group > 1:
                group_str = str(group)
                for i in range(len(group_str)):
                    chars[w] = group_str[i]
                    w += 1
            r += group
        return(w)





        