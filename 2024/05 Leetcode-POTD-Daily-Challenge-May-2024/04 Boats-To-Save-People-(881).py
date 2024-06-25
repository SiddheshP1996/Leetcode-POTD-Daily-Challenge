class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)

        def execute(left, right):
            if left > right:
                return 0
            if people[left] + people[right] <= limit:
                return 1 + execute(left + 1, right - 1)
            else:
                return 1 + execute(left, right - 1)

        return execute(0, n - 1)
