# Intuition
'''
1. arr[0] = 1
2. Each adjacent element differs by at most 1
3. Decrease any value, but can't increase
4. Rearrange values
'''

''' Algorithm
1. Sort arr in ascending order
2. initialize ans = 1
3. Iterate i over the indices of arr, starting from i=1:
    if arr[i] >= ans + 1, increment ans
    return ans
'''

from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr:List[int])->int:
        pass


arr = [2,1,77,123,43,16,7]
sln = Solution()
print(sln.maximumElementAfterDecrementingAndRearranging(arr))