class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            minimumElement = min(arr)
            maximumElement = max(arr)

            if (maximumElement - minimumElement) % (len(arr) - 1) != 0:
                return False

            diff = (maximumElement - minimumElement) / (len(arr) - 1)

            arrSet = set(arr)
            curr = minimumElement + diff
            while curr < maximumElement:
                if curr not in arrSet:
                    return False

                curr += diff

            return True

        results = []
        for i in range(len(l)):
            arr = nums[l[i]: r[i] + 1]
            results.append(check(arr))

        return results
