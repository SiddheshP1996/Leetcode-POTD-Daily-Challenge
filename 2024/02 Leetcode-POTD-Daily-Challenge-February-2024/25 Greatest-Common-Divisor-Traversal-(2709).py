from collections import deque

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if 1 in nums:
            return False

        nums = deque(set(nums))
        
        while True:
            travel_difference = []
            if len(nums) == 1:
                return True

            number_search = nums.popleft()

            while (g := gcd(number_search, aside := nums.popleft())) == 1:
                travel_difference.append(aside)
                if not nums:
                    return False

            nums.extend(travel_difference)
            nums.append(number_search * aside // g)
