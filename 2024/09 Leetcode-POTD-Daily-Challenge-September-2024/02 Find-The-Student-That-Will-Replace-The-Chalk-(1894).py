class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        remainder = k % total
        for i, value in enumerate(chalk):
            remainder -= value
            if remainder < 0:
                return i
        return -1
