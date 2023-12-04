# Solution 1

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            t = str(i) * 3
            if t in num:
                return t
        return ""

# Solution 2

"""
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1,-1):
            t = "".join(str(x) for x in [i,i,i])
            if num.find(t) != -1:
                return t
        return ""
"""
