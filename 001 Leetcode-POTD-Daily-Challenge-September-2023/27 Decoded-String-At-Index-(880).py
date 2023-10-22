class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = i = 0
        while length < k:
            if s[i].isdigit():
                length *= int(s[i])
            else:
                length += 1
            i += 1
        for l in range(i - 1, -1, -1):
            if s[l].isdigit():
                length //= int(s[l])
                k %= length
            else:
                if k == 0 or k == length:
                    return s[l]
                length -= 1
