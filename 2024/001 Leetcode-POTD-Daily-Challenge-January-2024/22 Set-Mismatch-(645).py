class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        repeated_and_missing_number = set()
        for i in range(len(nums)):
            if nums[i] in repeated_and_missing_number:
                result.append(nums[i])
            repeated_and_missing_number.add(nums[i])
        for i in range(1, len(nums) + 1):
            if i not in repeated_and_missing_number:
                result.append(i)
                break
        return result
