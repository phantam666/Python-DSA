from random import randint

class Train:
    def __init__(self, train_number, destination, departure_time, Seat_no):
        self.train_number = train_number
        self.destination = destination
        self.departure_time = departure_time
        self.seat_no = Seat_no


    def __str__(self):
        return f"Destination: {self.destination}, Departure Time: {self.departure_time}"
    
   
    def _getstatus_(self):
        return f"{self.train_number} is on time."
    
    
    def _getseatno__(self):
        return f"Seat no: {self.seat_no}."
       

t = Train("Train no - 1234", "New York", "10:00 AM", "A1")

print(t._getstatus_())  # Output: Train-XXXX is on time.
print(t.__str__())  # Output: Destination: New York, Departure Time: 10:00 AM
print(t._getseatno__())  # Output: Train XX .
