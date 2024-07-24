class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def translateInteger(num: int) -> int:
            if num == 0:
                return mapping[0]
            result: int = 0
            currentMultiple: int = 1
            while num > 0:
                digit = num % 10
                num //= 10
                result = mapping[digit] * currentMultiple + result
                currentMultiple *= 10

            return result

        numberMapping: dict[int, int] = {}
        for num in nums:
            numberMapping[num] = translateInteger(num)
        nums.sort(key=lambda val: numberMapping[val])

        return nums
