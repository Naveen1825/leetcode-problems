class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        return sum(abs(seat - student) for seat, student in zip(sorted(seats), sorted(students)))
        