class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ans, sol = [], []
        n = len(digits)

        def _backtrack(i=0):
            if i == n:
                ans.append(''.join(sol))
                return()
            
            for letter in chMap[digits[i]]:
                sol.append(letter)
                _backtrack(i+1)
                sol.pop()


        _backtrack(0)
        return(ans)            