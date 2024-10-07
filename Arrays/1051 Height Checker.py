class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = heights
        height = sorted(heights)
        count = 0
        for i in range(len(expected)):
            if expected[i] != height[i]:
                count += 1
        return count