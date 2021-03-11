import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [0] + [math.inf]*(len(nums)-1)
        for i in range(len(nums)-1):
            jump_range = nums[i]
            for j in range(jump_range):
                if i+j+1 > len(nums) - 1:
                    break
                memo[i+j+1] = min(memo[i] + 1, memo[i+j+1])
        return(memo[-1])
