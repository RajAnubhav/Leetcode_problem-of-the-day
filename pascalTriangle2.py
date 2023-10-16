class Solution:
    def getRow(self, rowIndex:int):
        output = [1]
        for i in range(1, rowIndex+1):
            output.append(1)
            for j in range(len(output)-2, 0, -1):
                output[j] += output[j-1]
        return output
    
rowIndex = 5
sln = Solution()
print(sln.getRow(rowIndex))