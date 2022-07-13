class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #O(n^2) check every combination of two values & see if they sum up to the target
        #O(log n) sort
        
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values: return [values[target-value], idx]
            else: values[value] = idx