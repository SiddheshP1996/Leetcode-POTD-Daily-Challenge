class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # initial step
        arr = [nums.pop(0)]
            # iterate through nums
        for n in nums:
            if n > arr[-1]:
                arr.append(n)
            else:
                arr[bisect_left(arr, n)] = n
        # return the length of arr
        return len(arr)
