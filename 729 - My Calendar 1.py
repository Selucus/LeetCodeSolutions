"""class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for index,item in enumerate(self.bookings):
            if(start<=item[0]):
                if(end<item[0]):
                    self.bookings.insert(index,[start,end])
                    return True
                else:
                    return False
            elif(start<item[1]):
                return False
        self.bookings.append([start,end])
        return True
                

myCalendar = MyCalendar();
print(myCalendar.book(10, 20))
print(myCalendar.book(15, 25)) 
print(myCalendar.book(20, 30))      """
import bisect
class MyCalendar:

    def __init__(self):
        self.bookings = [(-1,-1),(float('inf'),float('inf'))]

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_left(self.bookings,(start,end))

        if start < self.bookings[index-1][1]:
            return False
        if end > self.bookings[index][0]:
            return False

        self.bookings.insert(index,(start,end))
        return True        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

