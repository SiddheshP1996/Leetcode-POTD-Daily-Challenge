class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        # Initialize a stack to store potential '3' values.
        stack = []

        # Initialize a variable to keep track of the maximum '2' value found so far.
        max_2 = float('-inf')

        # Traverse the array from right to left.
        for i in range(n - 1, -1, -1):
            # If the current number is greater than the maximum '2' value, return True.
            if nums[i] < max_2:
                return True

            # While the stack is not empty and the current number is greater than the last element in the stack,
            # update the maximum '2' value with the last element in the stack.
            while stack and nums[i] > stack[-1]:
                max_2 = stack.pop()

            # Add the current number to the stack.
            stack.append(nums[i])

        return False
