class Ride:
    def __init__(self,user,distance):
        self.user = user
        self.distance = distance
    def fare(self):
        print(self.distance)
        print("This is for calculation of fare.")

class BikeRide(Ride):
    def __inti__(selfself,user,distance):
        super.__init__(user.distance)
    def fare(self):
        print("This is bike fare", self.distance * 50)

class CarRide(Ride):
    def __inti__(selfself,user,distance):
        super.__init__(user.distance)
    def fare(self):
        print("This is car fare", self.distance * 100)

bike = BikeRide("Aiswarya", 5)
bike.fare()
car = CarRide("Ayushma",15)
car.fare()