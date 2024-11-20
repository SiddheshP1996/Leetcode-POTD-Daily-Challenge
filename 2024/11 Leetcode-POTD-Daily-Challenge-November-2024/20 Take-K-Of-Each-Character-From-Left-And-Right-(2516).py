class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limits = {c: s.count(c) - k for c in 'abc'}
        if any(x < 0 for x in limits.values()):
            return -1

        counts = {c: 0 for c in 'abc'}
        result = left = 0
        for right, c in enumerate(s):
            counts[c] += 1
            while counts[c] > limits[c]:
                counts[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)

        return len(s) - result
