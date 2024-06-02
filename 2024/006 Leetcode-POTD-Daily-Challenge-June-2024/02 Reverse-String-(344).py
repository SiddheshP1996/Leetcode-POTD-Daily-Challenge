class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left = 0
        right = n - 1

        def swap(i, j):
            temporary = s[i]
            s[i] = s[j]
            s[j] = temporary

        while left <= right:
            swap(left, right)
            left += 1
            right -= 1
