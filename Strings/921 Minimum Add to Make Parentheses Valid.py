class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_l = 0
        count_r = 0
        for i in s:
            if i == '(':
                count_l += 1
            else:
                if count_l > 0:
                    count_l -= 1
                else:
                    count_r += 1
        return count_r + count_l
        