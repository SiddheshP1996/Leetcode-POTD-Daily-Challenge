class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize a list to store the number of combinations for each target value.
        dp = [0] * (target + 1)

        # There is one combination to reach target 0, which is not selecting any element.
        dp[0] = 1

        # Iterate through all target values from 1 to the given target.
        for i in range(1, target + 1):
            # For each target, iterate through all elements in nums.
            for num in nums:
                # If the current target value can be achieved by adding num,
                # update the number of combinations for the current target.
                if i - num >= 0:
                    dp[i] += dp[i - num]

        # The result is stored in dp[target].
        return dp[target]