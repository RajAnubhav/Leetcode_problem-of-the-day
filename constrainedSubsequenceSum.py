from collections import deque
class Solution:
    def constrainedSubsequenceSum(self, nums, k):
        # here using sliding window + dynamic programming
        # Initialize a deque to track max sum in a window of size k
        dq = deque()

        # Loop through each number in nums
        for i in range(len(nums)):

            # Add max sum from last k positions or 0 if deque is empty
            nums[i] += nums[dq[0]] if dq else 0

            # Ensure deque is in decreasing order and within window size
            while dq and (i-dq[0]>=k or nums[i]>=nums[dq[-1]]):
                dq.pop() if nums[i] >= nums[dq[-1]] else dq.popleft()

            # Append positive number to the deque
            if nums[i] > 0:
                dq.append(i)

        # Return the max value from modified nums
        return max(nums)
    
sln = Solution()
nums = [10, -2, -10, -5, 20]
k = 2
print(sln.constrainedSubsequenceSum(nums, k))