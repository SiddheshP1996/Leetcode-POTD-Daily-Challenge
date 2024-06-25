class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        relativeOrderDict = {}
        n = len(arr1)
        m = len(arr2)
        
        for i in range(m):
            relativeOrderDict[arr2[i]] = i
            
        sortRelative = []
        remaining = []
        
        for i in range(n):
            num = arr1[i]
            if num in relativeOrderDict:
                sortRelative.append((relativeOrderDict[num], num))
            else:
                remaining.append(num)
                
        sortRelative.sort()
        remaining.sort()
        result = []
            
        for i in range(len(sortRelative)):
            result.append(sortRelative[i][1])
            
        for n in remaining:
            result.append(n)
            
        return result
