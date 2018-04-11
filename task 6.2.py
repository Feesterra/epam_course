import abc


class Vehicle(metaclass=abc.ABCMeta):
    """Class can represent different vehicles.
    :param name: vehicle's name
    :param year: date of release
    :type year: int from 1900 to 2018
    :param model: vehicle's model
    :param km: mileage
    :type km: int"""

    def __init__(self, name, year, model, km):
        self.name = name
        self.model = model

        try:
            self.year = int(year)
            self.km = int(km)
        except ValueError as e:
            print("Year and number of kilometers must be numbers")
        if self.year < 1900 or self.year > 2018:
            raise ValueError("invalid year")
        if km < 0:
            raise ValueError("Non-negative km required")
        self.price = None

    @classmethod
    def vehicle_type(cls):
        """Returns class name."""

        return cls.__name__

    @staticmethod
    def is_motorcycle(self):
        """Check if vehicle is motorcycle (according to the number of wheels."""

        if self.wheels == 2:
            return True
        else:
            return False

    def purchase_price(self):
        """Calculates price (unknown currency)."""

        self.price = float("{0:.2f}".format(0.1 * self.km))
        return self.price


class Car(Vehicle):
    """Represents a car."""

    def __init__(self, name, year, model, km):
        Vehicle.__init__(self, name, year, model, km)
        self.wheels = 4


class Truck(Vehicle):
    """Represents a truck."""

    def __init__(self, name, year, model, km, wheels):
        Vehicle.__init__(self, name, year, model, km)
        if wheels % 2 == 0:
            self.wheels = wheels
        else:
            raise ValueError("Number of wheels must be even.")


class Motorcycle(Vehicle):
    """Represents a motorcycle."""

    def __init__(self, name, year, model, km):
        Vehicle.__init__(self, name, year, model, km)
        self.wheels = 2


class Bus(Vehicle):
    """Represents a bus."""

    def __init__(self, name, year, model, km):
        Vehicle.__init__(self, name, year, model, km)
        self.wheels = 6


if __name__ == '__main__':
    lada = Car("lasto4ka", year=2018, model="lada", km=12)
    lada.purchase_price()
    print(lada.vehicle_type(), lada.year, lada.name, lada.model, lada.wheels, lada.price)
    print(Vehicle.is_motorcycle(lada))

    motik = Motorcycle("vasily", 2015, "Yamaha", km=50)
    motik.purchase_price()
    print(motik.vehicle_type(), motik.name, motik.model, motik.wheels, motik.price)
    print(Vehicle.is_motorcycle(motik))

    gruzovik = Truck('amerika', year=2010, model="MAN", km=120, wheels=10)
    gruzovik.purchase_price()
    print(gruzovik.vehicle_type(), gruzovik.year, gruzovik.name, gruzovik.model, gruzovik.wheels, gruzovik.price)
    print(Vehicle.is_motorcycle(gruzovik))

