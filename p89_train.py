class train:
      def __init__(self, name, fare, seats):
            self.name = name
            self.fare = fare
            self.seats = seats
      
      def getStatus(self):
            print(f"The name of the train is {self.name}")
            print(f"the seats available in the train are {self.seats}")

      def fareInfo(self):
            print(f"the fare of the train for this journey {self.fare}")

      def bookTicket(self):
            if(self.seats>0):
                  print(f"Your ticket has been booked ! Your seat number is {self.seats}")
                  self.seats = self.seats - 1
            else:
                  print("bookings are full thanks")

      def cancleTicket(self):#pending
            print(f"Your ticket has been canceled is : {self.seats}")
            self.seats = self.seats +1


interCity = train("InterCity Exoress :  140123", 90, 10)
interCity.getStatus()
interCity.fareInfo()
interCity.bookTicket()
interCity.bookTicket()
interCity.getStatus()
interCity.cancleTicket()
interCity.getStatus()
