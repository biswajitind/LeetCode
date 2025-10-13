class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    
        result = [[1]]
        if numRows == 1:
            return(result)
        
        for row_num in range(2, numRows + 1):
            prev_row = result[row_num - 2]
            tmp_list = []
            for i in range(row_num):
                val1 = prev_row[i - 1] if i - 1 >= 0 else 0
                val2 = prev_row[i] if i < len(prev_row) else 0
                tmp_list.append(val1 + val2)
            result.append(tmp_list)
        return(result)


        
        