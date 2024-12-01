class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1: return True
        arrSet = set(arr) - {0}
        for a in arr:
            if 2 * a in arrSet: return True
        return False
