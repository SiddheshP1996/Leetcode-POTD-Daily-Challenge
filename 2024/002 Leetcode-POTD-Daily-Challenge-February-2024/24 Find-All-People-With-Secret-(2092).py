from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))
            
        earliest_time = [inf] * n
        earliest_time[0] = 0
        earliest_time[firstPerson] = 0

        # Queue for BFS.
        q = deque()
        q.append((0, 0))
        q.append((firstPerson, 0))

        # Do BFS
        while q:
            person, time = q.popleft()
            for secret_known_time, next_person in graph[person]:
                if secret_known_time >= time and earliest_time[next_person] > secret_known_time:
                    earliest_time[next_person] = secret_known_time
                    q.append((next_person, secret_known_time))
                    
        return [i for i in range(n) if earliest_time[i] != inf]
