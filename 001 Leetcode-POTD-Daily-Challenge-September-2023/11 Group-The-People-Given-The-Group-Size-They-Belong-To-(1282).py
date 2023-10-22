class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}  # Initialize an empty dictionary to store groups
        result = []  # Initialize an empty list to store the final result
        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []  # Create an empty list for this group size
            groups[size].append(i)  # Add the person to the corresponding group

            if len(groups[size]) == size:
                result.append(groups[size])  # If the group is full, add it to the result and reset it
                groups[size] = []

        return result
