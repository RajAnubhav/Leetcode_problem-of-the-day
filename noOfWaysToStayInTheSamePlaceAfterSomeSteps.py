class Solution:
    def numWays(self, steps:int, arrLen:int) -> int:
        def dfs(steps, idx):
            if idx-0 > steps:
                return 0
            
            if idx >= arrLen or idx < 0:
                return 0
            
            if steps == 0:
                if idx == 0:
                    return 1
                return 0
            
            tmp = 0
            tmp += dfs(steps-1, idx-1)
            tmp += dfs(steps-1, idx)
            tmp += dfs(steps-1, idx+1)

            return tmp%MOD
        
        MOD = 10**9+7

        return dfs(steps, 0)
    
sln = Solution()
steps = 4
arrLen = 2
print(sln.numWays(steps, arrLen))