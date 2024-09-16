class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        minutes = [convertToMinutes(timePeriod) for timePeriod in timePoints]
        minutes.sort()
        minuteDifference = float('inf')
        
        for i in range(1, len(minutes)):
            minuteDifference = min(minuteDifference, minutes[i] - minutes[i - 1])
        
        circularDiffreence = 1440 - minutes[-1] + minutes[0]
        minuteDifference = min(minuteDifference, circularDiffreence)
        
        return minuteDifference
