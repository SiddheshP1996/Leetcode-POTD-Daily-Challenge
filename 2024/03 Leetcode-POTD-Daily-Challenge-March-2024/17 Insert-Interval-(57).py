class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort()
        result = []

        for interval_start, interval_end in intervals:
            if len(result) > 0 and result[-1][-1] >= interval_start:
                result[-1][-1] = max(interval_end, result[-1][-1])
                continue
            result.append([interval_start, interval_end])
        return result
