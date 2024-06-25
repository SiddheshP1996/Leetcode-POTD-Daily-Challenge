class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum_num = max(nums)
        result = 0
        n = len(nums)

        maximum_index = [-1]
        for i in range(n):
            if nums[i] == maximum_num:
                maximum_index.append(i)
        
        index_size = len(maximum_index)

        for i in range(1, index_size - k + 1):
            left_side_num = maximum_index[i] - maximum_index[i - 1] - 1
            right_side_num = n - 1 - maximum_index[i + k - 1]
            result += (left_side_num + 1) * (right_side_num + 1)

        return result
