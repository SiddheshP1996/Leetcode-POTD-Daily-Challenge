class Solution:
    def minOperations(self, logs: List[str]) -> int:
        locateFolder = 0
        for logFolder in logs:
            if logFolder == "./":
                continue
            elif logFolder == "../":
                locateFolder = max(locateFolder - 1, 0)
            else:
                locateFolder += 1
        return locateFolder
