class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result_array_list = []
        current_array_list = []
        for num in nums:
            if len(current_array_list) == 0 or num - current_array_list[0] <= k:
                current_array_list.append(num)
                if len(current_array_list) == 3:
                    result_array_list.append(current_array_list)
                    current_array_list = []
            else:
                return []

        return result_array_list if len(current_array_list) == 0 else []
