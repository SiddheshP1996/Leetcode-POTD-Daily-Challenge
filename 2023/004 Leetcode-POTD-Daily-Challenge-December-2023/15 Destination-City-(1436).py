class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adjacentList = collections.defaultdict(list)
        for cityA, cityB in paths:
            adjacentList[cityA].append(cityB)
            if cityB not in adjacentList:
                adjacentList[cityB] = list()

        for cityFinal, cityB in adjacentList.items():
            if len(cityB) == 0:
                return cityFinal
        return ""
    