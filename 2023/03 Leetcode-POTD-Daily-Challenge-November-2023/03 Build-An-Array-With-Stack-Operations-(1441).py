class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        target.reverse()
        results = []
        for i in range(1, n + 1):
            while len(stack) > 0 and stack[-1] < target[-1]:
                results.append("Pop")
                stack.pop()

            results.append("Push")
            stack.append(i)
            if stack[-1] == target[-1]:
                target.pop()
                stack.append(10 ** 20)  # stop marker
            if len(target) == 0:
                break

        return results
