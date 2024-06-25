class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Create a list to store tuples of (count of ones in a row, row index)
        soldiers = []

        # Iterate through each row of the matrix
        for i in range(len(mat)):
            count = 0

            # Count the number of ones in the current row
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1

            # Append a tuple of count and row index to the list
            soldiers.append((count, i))

        # Sort the list based on the count of ones
        soldiers.sort()

        # Create a list to store the k weakest row indices
        weakest = []

        # Iterate through the sorted list to extract the k weakest rows
        for weakSoldier in soldiers[:k]:
            weakest.append(weakSoldier[1])

        # Return the list containing the k weakest row indices
        return weakest