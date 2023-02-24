from datetime import date, timedelta, datetime

class Apartment:
    def __init__(self, id = 0, address = "", capacity = 0, price = 0) -> None:
        self.id = id
        self.address = address
        self.capacity = capacity
        self.price = price

    def __str__(self) -> str:
        return "--Apartment--" \
            + "\nID: " + str(self.id) \
            + "\nAddress: " + self.address \
            + "\nCapacity: " + str(self.capacity) \
            + "\nPrice: " + str(self.price) + "\n"

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
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        try:
            self._capacity = int(value)
            if int(value) < 0:
                raise ValueError("Capacity must be an integer >= 0 ")
        except ValueError:
            raise

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        try:
            self._price = int(value)
            if int(value) < 0:
                raise ValueError("Price must be an integer >= 0 ")
        except ValueError:
            raise


