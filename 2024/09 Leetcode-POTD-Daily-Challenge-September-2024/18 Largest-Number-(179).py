class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arrayString = list(map(str, nums))

        arrayString.sort(key = lambda x: (x * 10), reverse = True)

        if arrayString[0] == "0":
            return "0"
        
        largestNumStr = ''.join(arrayString)

        return largestNumStr
