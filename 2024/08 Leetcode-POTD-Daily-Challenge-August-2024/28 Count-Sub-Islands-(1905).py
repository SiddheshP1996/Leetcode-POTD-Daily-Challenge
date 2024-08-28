class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.num_rows, self.num_cols = len(grid2), len(grid2[0])
        totalCells = self.num_rows * self.num_cols
        self.island_root = list(range(totalCells))
        self.island_status = [0] * totalCells

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if grid2[row][col] == 1:
                    current_index = row * self.num_cols + col
                    if col + 1 < self.num_cols and grid2[row][col + 1] == 1:
                        self.unionIslands(current_index, current_index + 1)
                    if row + 1 < self.num_rows and grid2[row + 1][col] == 1:
                        self.unionIslands(current_index, current_index + self.num_cols)

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if grid2[row][col] == 1 and grid1[row][col] == 0:
                    rootIndex = self.findIslandRoot(row * self.num_cols + col)
                    self.island_status[rootIndex] = 2

        subIslandCount = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if grid2[row][col] == 1:
                    rootIndex = self.findIslandRoot(row * self.num_cols + col)
                    if self.island_status[rootIndex] == 0:
                        subIslandCount += 1
                        self.island_status[rootIndex] = 1

        return subIslandCount

    def findIslandRoot(self, x: int) -> int:
        if self.island_root[x] != x:
            self.island_root[x] = self.findIslandRoot(self.island_root[x])
        return self.island_root[x]

    def unionIslands(self, x: int, y: int):
        rootX = self.findIslandRoot(x)
        rootY = self.findIslandRoot(y)
        if rootX != rootY:
            self.island_root[rootY] = rootX
