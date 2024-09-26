class MyCalendar:

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
print(myCalendar.book(20, 30))      