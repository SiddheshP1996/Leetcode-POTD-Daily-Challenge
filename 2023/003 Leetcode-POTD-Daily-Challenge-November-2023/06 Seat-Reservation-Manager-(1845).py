import heapq


class SeatManager:

    def __init__(self, n: int):
        self.freeSeats = [i for i in range(1, n + 1)]
        self.reservedSeats = set()

    def reserve(self) -> int:
        seat = heapq.heappop(self.freeSeats)
        self.reservedSeats.add(seat)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        if not (seatNumber in self.reservedSeats):
            return
        self.reservedSeats.discard(seatNumber)
        heapq.heappush(self.freeSeats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
