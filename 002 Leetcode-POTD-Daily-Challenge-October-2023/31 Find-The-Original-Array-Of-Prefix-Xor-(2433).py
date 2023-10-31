class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        N = len(pref)
        results = [0] * N
        results[0] = pref[0]

        for i in range(1, N):
            results[i] = pref[i-1] ^ pref[i]
        return results
