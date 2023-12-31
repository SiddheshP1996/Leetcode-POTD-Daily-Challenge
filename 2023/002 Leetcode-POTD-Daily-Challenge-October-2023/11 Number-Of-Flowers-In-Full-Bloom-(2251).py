class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        startPoint = sorted([starting for starting, ending in flowers])
        endPoint = sorted([ending for starting, ending in flowers])
        return [bisect_right(startPoint, testCase) - bisect_left(endPoint, testCase) for testCase in people]
