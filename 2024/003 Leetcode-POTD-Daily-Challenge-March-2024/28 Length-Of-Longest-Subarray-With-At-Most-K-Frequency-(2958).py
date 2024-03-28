import sortedcontainers
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        frequency_count = collections.defaultdict(int)
        left_node_value = 0
        right_node_value = 0
        result = 0
        while right_node_value < n:
            frequency_count[nums[right_node_value]] += 1
            while left_node_value <= right_node_value and frequency_count[nums[right_node_value]] > k:
                frequency_count[nums[left_node_value]] -= 1
                left_node_value += 1
            result = max(result, right_node_value - left_node_value + 1)
            right_node_value += 1
        return result
