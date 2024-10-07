class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in s:
            if stack:
                if stack[-1] == 'A' and i =='B':
                    stack.pop()
                    continue
                if stack[-1] == 'C' and i =='D':
                    stack.pop()
                    continue
            stack.append(i)
        return len(stack)