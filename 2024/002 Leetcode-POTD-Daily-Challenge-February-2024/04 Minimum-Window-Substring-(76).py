class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_1 = collections.defaultdict(int)
        for counts in t:
            count_1[counts] += 1

        count_window = collections.defaultdict(int)
        def compare_count():
            for counts in count_1.keys():
                if count_window[counts] < count_1[counts]:
                    return False
            return True

        left_item = 0
        right_item = 0
        n = len(s)
        result = (0, n)
        while right_item < n:
            count_window[s[right_item]] += 1
            while compare_count() and left_item <= right_item:
                if result[1] - result[0] > right_item - left_item:
                    result = (left_item, right_item)
                count_window[s[left_item]] -= 1
                left_item += 1
            right_item += 1
        if result[1] == n:
            return ""
        return s[result[0]:(result[1] + 1)]
