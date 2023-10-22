class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Initialize an empty result string
        answer = ""
        # Initialize a dictionary to store the last occurrence index of each character
        last_occurrence = {}
        # Populate the last_occurrence dictionary with the last index of each character
        for i, char in enumerate(s):
            last_occurrence[char] = i
        # Iterate through the characters in the input string
        for i, char in enumerate(s):
            if char not in answer:
                while answer and char < answer[-1] and i < last_occurrence[answer[-1]]:
                    answer = answer[:-1]
                # Append the current character to res.
                answer += char
        return answer
