class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        row = [1]  # Initialize the first row with a single 1

        for i in range(1, rowIndex + 1):
            new_row = [1]  # Start with the first 1 in each row
            for j in range(1, i):
                new_row.append(row[j - 1] + row[j])  # Compute the new value using the previous row
            new_row.append(1)  # End with the last 1 in each row
            row = new_row  # Update the row with the new values

        return row
