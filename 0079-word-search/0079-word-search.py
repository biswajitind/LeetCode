class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m_len = len(board)
        n_len = len(board[0])
        word_len = len(word)

        def _dfs(m,n, index):

            if m < 0 or m >= m_len or n < 0 or n >= n_len:
                return(False)

            if index >= word_len:
                return(False)

            ch = board[m][n]
            if ch != word[index]:
                return(False)
            else:
                if index == word_len - 1:
                    return(True)

            for x, y in [[m-1, n],[m+1, n],[m, n-1],[m, n+1]]:
                board[m][n] = '#'
                ret = _dfs(x, y, index+1)
                board[m][n] = ch
                if ret:
                    return(True)

            return(False)

        for i in range(m_len):
            for j in range(n_len):
                if _dfs(i,j, 0):
                    return(True)
    
        return(False)