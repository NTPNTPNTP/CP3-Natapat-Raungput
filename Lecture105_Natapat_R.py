class Vehicle:
    licenseCode = ""
    serialCode = ""

    def turnOnAirConditioner(self):
        print("Turn On : Air")


class Pickup(Vehicle):
    pass;


class Car(Vehicle):
    pass;


class Van(Vehicle):
    pass;


class Estate(Vehicle):
    pass;


pickup = Pickup()
pickup.turnOnAirConditioner()

car = Car()
car.turnOnAirConditioner()

van = Van()
van.turnOnAirConditioner()

estate = Estate()
estate.turnOnAirConditioner()
