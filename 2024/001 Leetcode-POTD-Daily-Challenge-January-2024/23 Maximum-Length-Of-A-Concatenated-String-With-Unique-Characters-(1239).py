class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result_of_max_length = [0]
        self.dfs(arr, "", 0, result_of_max_length)
        return result_of_max_length[0]

    def dfs(self, arr, path, index, result_of_max_length):
        if self.isUniqueChars(path):
            result_of_max_length[0] = max(result_of_max_length[0], len(path))

        if index == len(arr) or not self.isUniqueChars(path):
            return

        for i in range(index, len(arr)):
            self.dfs(arr, path + arr[i], i + 1, result_of_max_length)

    def isUniqueChars(self, string):
        character_set = set()
        for character in string:
            if character in character_set:
                return False
            character_set.add(character)
        return True
