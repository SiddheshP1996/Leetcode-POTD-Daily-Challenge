class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(maxProducts: int) -> bool:
            storesNeeded = sum((quantity + maxProducts - 1) // maxProducts for quantity in quantities)
            return storesNeeded <= n

        left, right = 1, max(quantities)
        
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
