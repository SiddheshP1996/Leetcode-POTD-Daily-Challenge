class Solution:
    def findComplement(self, num: int) -> int:
        bitLength = num.bit_length()
        
        mask = (1 << bitLength) - 1
        
        return num ^ mask
