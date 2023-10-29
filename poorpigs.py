from math import ceil, log


class Solution:
    def poorPigs(self, buckets:int, minutesToDie:int, minutesToTest:int)->int:
        return ceil(log(buckets)/log(int(minutesToDie/minutesToTest)+1))



s = Solution()
buckets = 4
minutesToDie ,minutesToTest = 15, 15
print(s.poorPigs(buckets, minutesToDie, minutesToTest))