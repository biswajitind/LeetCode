class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_list = [chr(i) for i in range(ord('0'), ord('9') + 1)]
        valid_list.extend([chr(i) for i in range(ord('a'), ord('z') + 1)])
        valid_list.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
        valid = set(valid_list)
        # Two pointer approach.
        start = 0
        end = len(s) - 1

        while start < end:
            if not s[start] in valid:
                start += 1
                continue
            if not s[end] in valid:
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return(False)
            start += 1
            end -= 1
        return(True)
