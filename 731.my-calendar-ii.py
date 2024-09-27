#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#

# @lc code=start

class MyCalendarTwo:

    def __init__(self):
        self.bookings = [(-1,-1),(float("inf"),float("inf"))]
        self.doubleBookings = [(-1,-1),(float("inf"),float("inf"))]

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_left(self.doubleBookings,(start,end))

        if start < self.doubleBookings[index-1][1]:
            return False
        if end > self.doubleBookings[index][0]:
            return False

        i = bisect.bisect_left(self.bookings,(start,end))
        if start < self.bookings[i-1][1]:
            newDoubleBooking = (start,self.bookings[i-1][1])
            new = bisect.bisect_left(self.doubleBookings,newDoubleBooking)
            self.doubleBookings.insert(new,newDoubleBooking)
        if end > self.bookings[i][0]:
            newDoubleBooking = (self.bookings[i][0],end)
            new = bisect.bisect_left(self.doubleBookings,newDoubleBooking)
            self.doubleBookings.insert(new,newDoubleBooking)
        self.bookings.insert(i,(start,end))
        return True        
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end

