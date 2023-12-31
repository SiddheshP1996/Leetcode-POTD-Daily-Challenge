class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        results = [""] * n
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        vowelsQueue = []
        for i in range(n):
            c = s[i]
            if c in vowels:
                vowelsQueue.append((c,i))
            else:
                results[i] = c
        vowelsQueue.sort(reverse = True)
        for i in range(n):
            if results[i] == "":
                results[i] = vowelsQueue.pop()[0]
        return "".join(results)
