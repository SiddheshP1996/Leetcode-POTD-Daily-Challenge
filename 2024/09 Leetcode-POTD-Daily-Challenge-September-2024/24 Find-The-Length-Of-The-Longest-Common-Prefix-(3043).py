class Trie:
    def __init__(self, nums):
        self._dictionary = {}
        for element in nums:
            self._addElement(element)
    
    def _addElement(self, element):
        dictionary = self._dictionary
        for character in str(element):
            if character not in dictionary:
                dictionary[character] = {}
            dictionary = dictionary[character]
    
    def _findLength(self, element):
        dictionary = self._dictionary
        for i, character in enumerate(str(element)):
            if character not in dictionary:
                return i
            dictionary = dictionary[character]
        return i + 1

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie(set(arr1))
        return max(
            trie._findLength(element)
            for element in set(arr2)
        )
