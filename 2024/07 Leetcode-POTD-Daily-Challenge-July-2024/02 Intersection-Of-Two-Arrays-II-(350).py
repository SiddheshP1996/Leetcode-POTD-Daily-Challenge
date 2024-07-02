class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []    
        
        numberOne, numberTwo = sorted(nums1), sorted(nums2)
        i = j = 0
        
        while i < len(numberOne) and j < len(numberTwo):
            if numberOne[i] == numberTwo[j]:
                result.append(numberOne[i])
                i += 1
                j += 1
            elif numberOne[i] < numberTwo[j]:
                i += 1
            else:
                j += 1
                
        return result
