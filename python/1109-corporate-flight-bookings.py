# medium
'''2022-01-09'''

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * (n+1)  # last element is dumb
        for first, last, num in bookings:
            flights[first-1] += num  # 1-base
            flights[last] -= num
        for i in range(1, n):
            flights[i] += flights[i-1]
        return flights[:-1]
