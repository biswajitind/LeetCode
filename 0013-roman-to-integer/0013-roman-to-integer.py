class Solution:
    def romanToInt(self, s: str) -> int:
        mapList = [
            ['I', '1'],
            ['IV', '4'],
            ['V', '5'],
            ['IX', '9'],
            ['X', '10'],
            ['XL', '40'],
            ['L', '50'],
            ['XC', '90'],
            ['C', '100'],
            ['CD', '400'],
            ['D', '500'],
            ['CM', '900'],
            ['M', '1000']
        ]

        i = 0 
        result = 0
        while i < len(s):
            for key, val in reversed(mapList):
                if s[i:].startswith(key):
                    result += int(val)
                    i += len(key)
                    break
        return(result)




