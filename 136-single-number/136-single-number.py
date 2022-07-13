class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
Intuition:
Xor of any two num gives the difference of bit as 1 and same bit as 0.
Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
So, we will always get the single element because all the same ones will evaluate to 0 and 0^single_number = single_number.
        """
        xor = 0
        for e in nums:
            xor = xor ^ e
        return xor
        