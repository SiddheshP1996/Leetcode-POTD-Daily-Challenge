class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = collections.Counter(tasks)
        maximum_frequency = max(frequency.values())
        frequency = list(frequency.values())
        maximum_frequency_ele_count = 0
        i = 0
        while( i < len(frequency)):
            if frequency[i] == maximum_frequency:
                maximum_frequency_ele_count += 1
            i += 1
            
        result = (maximum_frequency - 1) * (n + 1) + maximum_frequency_ele_count
        
        return max(result, len(tasks))
