class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        m = len(nums[0])
        nums = set(nums)

        def goFindString(i, arr):
            if i == m:
                number = "".join(arr)
                if number in nums:
                    return False, ""
                else:
                    return True, number
            arr.append("0")
            found, number = goFindString(i + 1, arr)
            if found:
                return found, number
            arr.pop()
            arr.append("1")
            found, number = goFindString(i + 1, arr)
            arr.pop()
            return found, number

        return goFindString(0, [])[1]
