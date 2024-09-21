class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        currentElement = 1
        
        for element in range(n):
            result.append(currentElement)
            
            if currentElement * 10 <= n:
                currentElement *= 10
            else:
                if currentElement >= n:
                    currentElement //= 10
                currentElement += 1
                
                while currentElement % 10 == 0:
                    currentElement //= 10
                
        return result
