class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        res, mx = 0,0
        for e in nums:
            hashmap[e] = 1 + hashmap.get(e,0)
            res = e if hashmap[e] > mx else res
            mx = max(hashmap[e], mx)
        return res