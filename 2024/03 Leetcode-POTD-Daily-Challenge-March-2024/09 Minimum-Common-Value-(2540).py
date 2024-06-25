class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pointerOne = 0
        pointerTwo = 0

        while pointerOne < len(nums1) and pointerTwo < len(nums2):
            if nums1[pointerOne] == nums2[pointerTwo]:
                return nums1[pointerOne]
            if nums1[pointerOne] < nums2[pointerTwo]:
                pointerOne += 1
            else:
                pointerTwo += 1
        return -1
