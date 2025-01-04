from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def mileage(self):
        pass

class suzuki(car):
    def mileage(self):
        print("Mileage is 20kmph")

class tesla(car):
    def mileage(self):
        print("Mileage is 30kmph")

s1=suzuki()
s1.mileage()
t1=tesla()
t1.mileage()
c1=car()
c1.mileage()

#we can't create object for abstract class
