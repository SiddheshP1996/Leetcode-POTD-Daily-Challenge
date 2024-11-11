class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = []

        for num in range(2, 1000):
            for i in primes:
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
        
        primes = [0] + primes
        previousMin = 0
        
        for number in nums:
            if number <= previousMin:
                return False
            
            nextPreviousMin = 0
            for prime in primes:
                if prime < number:
                    if number - prime > previousMin:
                        nextPreviousMin = number-prime
                else:
                    break
            previousMin = nextPreviousMin
        return True
