class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        n = len(nums)

        def execute(i, currentElement):
            if i >= n:
                result.append(list(currentElement))
                return
            currentElement.append(nums[i])
            for j in range(i + 1, n + 1):
                execute(j, currentElement)
            currentElement.pop()

        for i in range(n):
            execute(i, [])
        return result
