class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i, j = 0, len(matrix) - 1
        while i < j:
            for step in range(j-i): 
                matrix[i][i+step], matrix[i+step][j], matrix[j][j-step], matrix[j-step][i] = matrix[j-step][i], matrix[i][i+step], matrix[i+step][j], matrix[j][j-step]
            i += 1
            j -= 1