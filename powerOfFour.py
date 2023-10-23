class Solution:
    def isPowerOfFour(self, n):
        return (n&n-1) == 0 and (n-1)%3 == 0
    
sln = Solution()
n = int(input())
print(sln.isPowerOfFour(n))