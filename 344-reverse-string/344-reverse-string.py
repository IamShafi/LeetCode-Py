class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        i, j = 0, len(s)-1
        while i < j:
               s[i], s[j] = s[j], s[i]
               i += 1
               j -= 1
        #range(start, stop, step)
        #enumerate(iterable, star = 0)
        for idx, ele in enumerate(s, start = 1):
            s[idx-1], s[-idx] = s[-idx], s[idx-1]
            if idx == len(s) // 2:
                break
        """
        def recur(l,r):
            if l<r:
                s[l], s[r] = s[r], s[l]
                recur(l+1, r-1)
        recur(0, len(s)-1)
        