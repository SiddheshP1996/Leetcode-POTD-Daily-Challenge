class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0]]
        
        for i in range(1, len(folder)):
            lastFolder = result[-1] + '/'
            
            if not folder[i].startswith(lastFolder):
                result.append(folder[i])
        
        return result
