class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = [[nums[0]]]
        n = len(nums)
        # Use Binary Seacrh
        for i in range(1, n):
            leftPointer = 0
            rightPointer = len(result)
            while leftPointer < rightPointer:
                middlePosition = (leftPointer + rightPointer) // 2
                if result[middlePosition][-1] == nums[i]:
                    leftPointer = middlePosition + 1
                else:
                    rightPointer = middlePosition
            if leftPointer == len(result):
                result.append([])
            result[leftPointer].append(nums[i])
        return result
