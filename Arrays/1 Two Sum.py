class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
    
        for i, num in enumerate(nums):
            check = target - num
            
            if check in hm:
                return [hm[check], i]
            
            hm[num] = i
        