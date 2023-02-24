from abc import ABC, abstractmethod

class Property(ABC):
    def __init__(self, id = 0, surface = 0, address = "") -> None:
        self.id = id
        self.surface = surface
        self.address = address

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        try:
            self._id = int(value)
            if int(value) < 0:
                raise ValueError("Id must be an integer >= 0 ")
        except ValueError:
            raise

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, value):
        try:
            self._surface = int(value)
            if int(value) < 0:
                raise ValueError("Surface must be an integer >= 0 ")
        except ValueError:
            raise

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @abstractmethod
    def calculate_tax(self):
        pass

    def __str__(self) -> str:
        return super().__str__()
        
class Apartment(Property):
    def __init__(self, id=0, surface=0, address="", floor = 0) -> None:
        super().__init__(id, surface, address)
        self.floor = floor

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        try:
            self._floor = int(value)
            if int(value) < 0:
                raise ValueError("Floor must be an integer >= 0 ")
        except ValueError:
            raise

    def __str__(self) -> str:
        ret = "--Apartment--" \
            + "\nSurface: " + str(self.surface) \
            + "\nFloor: " + str(self.floor) \
            + "\nAddress: " + self.address + "\n" 
        return ret

    def calculate_tax(self):
        return 1.3 * self.surface + 10 * self.floor + 150

class Store(Property):
    def __init__(self, id=0, surface=0, address="", commerciality = 0) -> None:
        super().__init__(id, surface, address)
        self.commerciality = commerciality

    @property
    def commerciality(self):
        return self._commerciality

    @commerciality.setter
    def commerciality(self, value):
        try:
            self._commerciality = int(value)
            if int(value) < 0 or int(value) > 5:
                raise ValueError("Commerciality must be an integer between 0 and 5 ")
        except ValueError:
            raise

    def __str__(self) -> str:
        ret = "--Store--" \
            + "\nSurface: " + str(self.surface) \
            + "\nCommerciality: " + str(self.commerciality) \
            + "\nAddress: " + self.address + "\n" 
        return ret

    def calculate_tax(self):
        return 2.5 * self.surface + 20 * self.commerciality + 100

class Plot(Property):
    def __init__(self, id=0, surface=0, address="", within_city_limits = True, cultivated = True) -> None:
        super().__init__(id, surface, address)
        self.within_city_limits = within_city_limits
        self.cultivated = cultivated

    @property
    def within_city_limits(self):
        return self._within_city_limits

    @within_city_limits.setter
    def within_city_limits(self, value):
        try:
            self._within_city_limits= bool(value)
        except ValueError:
            raise 

    @property
    def cultivated(self):
        return self._cultivated

    @cultivated.setter
    def cultivated(self, value):
        try:
            self._cultivated= bool(value)
        except ValueError:
            raise 

    def __str__(self) -> str:
        ret = "--Plot--" \
            + "\nSurface: " + str(self.surface) \
            + "\nWithin city limits: " + str(self.within_city_limits) \
            + "\nCultivated: " + str(self.cultivated) \
            + "\nAddress: " + self.address + "\n" 
        return ret

    def calculate_tax(self):
        return 0.3 * self.surface + 100 * self.cultivated \
            + 200 * self.within_city_limits


