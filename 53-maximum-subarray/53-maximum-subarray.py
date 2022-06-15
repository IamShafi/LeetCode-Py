class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        cur = 0
        for i in nums:
            if cur < 0:
                cur = 0
            cur += i
            mx = max(mx, cur)
        return mx
    
