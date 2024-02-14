class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_int = collections.deque()
        negative_int = collections.deque()
        n = len(nums)
        for int_number in nums:
            if int_number < 0:
                negative_int.append(int_number)
            else:
                positive_int.append(int_number)

        result = []
        while len(result) < n:
            if (len(result) == 0 or result[-1] < 0) and len(positive_int) > 0:
                result.append(positive_int.popleft())
            else:
                result.append(negative_int.popleft())
        return result
