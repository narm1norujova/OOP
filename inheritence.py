class Vehicle:
    def general_usage(self):
        print("general use: transportation")

class Car(Vehicle):
    def __init__(self):
        print("I am a car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use: commute to work, vacationwith family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I am a motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("specific use: road trip, racing")


c = Car()
# c.general_usage()
# c.specific_usage()


m = MotorCycle()
# m.general_usage()
# m.specific_usage()

print(isinstance(c, Car))
print(issubclass(Car, Vehicle))