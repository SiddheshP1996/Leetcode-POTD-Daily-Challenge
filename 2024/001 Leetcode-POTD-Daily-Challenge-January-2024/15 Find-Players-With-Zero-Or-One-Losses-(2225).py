class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        playerSeen = set()
        lostPlayerCount = collections.defaultdict(int)

        for match in matches:
            win,lose = match
            lostPlayerCount[lose] += 1
            playerSeen.add(win)
            playerSeen.add(lose)

        playerNeverLost = []
        playerOneLost = []
        playerSeen = sorted(playerSeen)

        for players in playerSeen:
            if lostPlayerCount[players] == 1:
                playerOneLost.append(players)
            elif lostPlayerCount[players] == 0:
                playerNeverLost.append(players)
        return [playerNeverLost,playerOneLost]