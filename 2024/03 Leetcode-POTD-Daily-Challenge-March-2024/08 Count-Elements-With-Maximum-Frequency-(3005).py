class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        top_max_freq = collections.Counter(nums)

        result = 0
        most_freq = top_max_freq.most_common()
        maximum = most_freq[0][1]

        for _, freq in most_freq:
            if freq == maximum:
                result += freq
            else:
                break
        return result
