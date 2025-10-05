class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split('/')
        print(pathList)
        resultList  = [] 
        for p in pathList:
            if p == '' or p == '.':
                continue
            if p == '..':
                if resultList:
                    resultList.pop()
            else:
                resultList.append(p)
        return('/' + '/'.join(resultList))
