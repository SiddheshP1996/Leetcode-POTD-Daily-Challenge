from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        counter = defaultdict(int)

        def execute(item, count):
            if item == n:
                return 1 if len(count) > 0 else 0
            num = nums[item]
            result = execute(item + 1, count)
            if (num - k) not in count:
                count[num] += 1
                result += execute(item + 1, count)
                count[num] -= 1
                if count[num] == 0:
                    count.pop(num)
            return result

        return execute(0, counter)
