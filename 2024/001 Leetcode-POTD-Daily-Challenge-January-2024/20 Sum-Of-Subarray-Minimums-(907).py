class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = ((10 ** 9) + 7)
        stack = []
        minimum_sum = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                middle_array = stack.pop()
                left_array_boundary = stack[-1] if stack else -1
                right_array_boundary = i

                count = (middle_array - left_array_boundary) * (right_array_boundary - middle_array) % mod

                minimum_sum += (count * arr[middle_array]) % mod
                minimum_sum %= mod
            stack.append(i)

        return int(minimum_sum)
