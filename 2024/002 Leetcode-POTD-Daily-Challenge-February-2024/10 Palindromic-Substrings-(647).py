class Solution:
    def countSubstrings(self, s: str) -> int:
        string_length, total_palin_count = len(s), 0
        for i in range(string_length):
            for left_palin, right_palin in [(i, i),(i, i + 1)]:
                while left_palin >= 0 and right_palin < string_length and s[left_palin] == s[right_palin]: left_palin -= 1; right_palin += 1
                total_palin_count += (right_palin - left_palin) // 2
        return total_palin_count
