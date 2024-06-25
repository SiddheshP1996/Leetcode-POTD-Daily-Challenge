class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def isPalindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        result = []

        def execute(i, currentItem):
            if i == n:
                result.append(list(currentItem))
                return
            for j in range(i, n):
                if isPalindrome(i, j):
                    currentItem.append(s[i:j + 1])
                    execute(j + 1, currentItem)
                    currentItem.pop()

        execute(0, [])
        return result
