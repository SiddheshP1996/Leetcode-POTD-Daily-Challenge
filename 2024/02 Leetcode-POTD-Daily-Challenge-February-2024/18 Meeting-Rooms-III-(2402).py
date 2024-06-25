from heapq import heappush
from collections import defaultdict

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        START = 1
        END = -1
        timeline = []
        counter = collections.defaultdict(int)
        meetingsMap = {}
        meetingsPriority = []
        for item in range(len(meetings)):
            startSearch, endSearch = meetings[item]
            meetingsMap[item] = [startSearch, endSearch, -1]
            meetingsPriority.append((startSearch, endSearch, item))
        heapq.heapify(meetingsPriority)

        free_rooms = [i for i in range(n)]
        for room_id in range(n):
            startSearch, endSearch, item = heapq.heappop(meetingsPriority)
            heapq.heappush(timeline, (startSearch, START, room_id, item))
            if len(meetingsPriority) == 0:
                break

        while len(timeline) > 0:
            time, event, room_id, id = heapq.heappop(timeline)
            if event == END:
                heapq.heappush(free_rooms, meetingsMap[id][2])
                if len(meetingsPriority) > 0:
                    startSearch, endSearch, item = heapq.heappop(meetingsPriority)
                    if time > startSearch:
                        delay = time - startSearch
                        duration = endSearch - startSearch
                        startSearch += delay
                        endSearch = startSearch + duration
                    meetingsMap[item][0] = startSearch
                    meetingsMap[item][1] = endSearch
                    heapq.heappush(timeline, (startSearch, START, room_id, item))
            else:
                room_id = heapq.heappop(free_rooms)
                counter[room_id] += 1
                room_time = meetingsMap[id][1]
                meetingsMap[id][2] = room_id
                heapq.heappush(timeline, (room_time, END, room_id, id))

        result = 0
        result_room = 0
        for item in range(n):
            if counter[item] > result:
                result = counter[item]
                result_room = item
        return result_room
