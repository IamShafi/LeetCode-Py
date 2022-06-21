class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack = []
        for i in ops:
            if i == 'C':
                stack.pop()
            elif i == 'D': #double the previous value
                stack.append(2 * stack[-1])
            elif i == '+': #sum of previous two
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
        