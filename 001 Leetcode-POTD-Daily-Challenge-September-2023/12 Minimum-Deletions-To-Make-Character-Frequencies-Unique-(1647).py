class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = sorted(Counter(s).values(), reverse = True)
        prev = keep = frequencies.pop(0)
        for freq in frequencies:
            freq = min(prev - 1, freq)
            if freq == 0: break
            keep += freq
            prev = freq
        return len(s) - keep