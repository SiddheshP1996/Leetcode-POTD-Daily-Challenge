from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    # Depth-first search function to find the itinerary
    def dfs(self, adj, result, s):
        # While there are destinations connected to the current airport
        while adj[s]:
            # Get the next destination
            v = heappop(adj[s])
            # Recursively explore this destination
            self.dfs(adj, result, v)
        # Add the current airport to the result
        result.append(s)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create an adjacency list to represent the flights
        adj = defaultdict(list)
        for t in tickets:
            heappush(adj[t[0]], t[1])

        # Initialize the result list
        result = []
        # Start the depth-first search from JFK (John F. Kennedy International Airport)
        self.dfs(adj, result, "JFK")
        # Reverse the result to get the correct itinerary
        result.reverse()
        # Return the itinerary
        return result
