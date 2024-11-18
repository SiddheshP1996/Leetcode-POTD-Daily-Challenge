class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        codeLength = len(code)
        if k == 0:
            return [0] * codeLength

        result = []
        nums = 3 * code
        for i in range(codeLength, 2 * codeLength):
            if k > 0:
                result.append(sum(nums[i + 1 : i + k + 1]))
            else:
                result.append(sum(nums[i + k : i]))
        return result
