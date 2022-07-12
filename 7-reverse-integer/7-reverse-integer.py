class Solution:
    def reverse(self, x: int) -> int:
        
        if x==0: return x
        revN = int( str(x)[::-1] ) if x>0 else -int( (str(x)[1:]) [::-1] )
        return revN if -2**31 <= revN <= 2**31 - 1 else 0
        