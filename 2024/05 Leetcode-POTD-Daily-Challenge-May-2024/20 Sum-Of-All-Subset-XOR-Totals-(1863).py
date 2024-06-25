class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        subsets = []

        def execute(i, currentElement):
            if i == n:
                subsets.append(list(currentElement))
            for j in range(i, n):
                currentElement.append(nums[i])
                execute(j + 1, currentElement)
                currentElement.pop()

        for i in range(n):
            execute(i, [])

        result = 0
        for subset in subsets:
            result_here = 0
            for x in subset:
                result_here ^= x
            result += result_here
        return result
