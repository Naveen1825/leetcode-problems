class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        bal = 0
        for ch in s:
            if ch == ']':
                count += 1
                if bal < count:
                    bal += 1
            else:
                count -= 1
        return (bal + 1) // 2
        