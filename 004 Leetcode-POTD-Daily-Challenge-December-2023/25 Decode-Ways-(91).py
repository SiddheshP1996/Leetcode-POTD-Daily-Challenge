class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        s = [int(c) for c in s]

        cache = {}

        def decodeMessage(mustCombineCharacterInteger, i):
            if i == n:
                return 1 if not mustCombineCharacterInteger else 0
            if (mustCombineCharacterInteger, i) in cache:
                return cache[(mustCombineCharacterInteger, i)]
            currentNumber = s[i]
            result = 0
            if mustCombineCharacterInteger:
                previousNumber = (s[i - 1] * 10)
                combined = previousNumber + currentNumber
                if 1 <= combined <= 26:
                    result = decodeMessage(False, i + 1)
                else:
                    result = 0
            else:
                if currentNumber != 0:  # If currentNumber is 0, we must combine it with the previous
                    result = decodeMessage(False, i + 1) \
                          + decodeMessage(True, i + 1)
            cache[(mustCombineCharacterInteger, i)] = result
            return result

        return decodeMessage(False, 0)