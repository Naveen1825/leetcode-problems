class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        lis = []
        lis1 = []

        for i in range(len(arr1)):
            if arr1[i] in arr2:
                lis.append(arr1[i])
        lis.sort(key=lambda ind: arr2.index(ind))

        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                lis1.append(arr1[i])
                
        lis1.sort()
        lis.extend(lis1)
        
        return lis