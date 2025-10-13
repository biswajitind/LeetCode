class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prow = [1]

        if rowIndex == 0:
            return(prow)
        for row in range(1, rowIndex + 2):
            crow = []
            for i in range(row):
                val1 = prow[i-1] if i-1 >= 0 else 0
                val2 = prow[i] if i < len(prow) else 0
                crow.append(val1 + val2)
            prow = crow
        return(prow)
            

        