class Ride:
    def __init__(self,user,distance):
        self.user = user
        self.distance = distance  #private used for encapsulation
    def get_distance(self):
        return self.distance
    def set_distance(self,distance):
        if distance > 0: self.__distance = distance
r = Ride("Aiswarya", 5)
r.set_distance(10)
print(r.get_distance())
