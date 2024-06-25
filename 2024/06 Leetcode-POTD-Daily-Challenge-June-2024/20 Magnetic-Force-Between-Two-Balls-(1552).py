class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = (position[-1] - position[0] + 1)
        n = len(position)

        def targetCount(target):
            count = 0
            minimumSeen = position[0]
            for i in range(1, n):
                difference = position[i] - minimumSeen
                if difference >= target:
                    count += 1
                    minimumSeen = position[i]
            return count >= (m - 1)

        result = 0
        while left < right:
            middle = (left + right) // 2
            if targetCount(middle):
                result = middle
                left = middle + 1
            else:
                right = middle
        return result
