from abc import ABC, abstractmethod
from datetime import date, timedelta, datetime
from multipledispatch import dispatch

BASE_PACKAGE_COST_FACTOR = 5
BASE_PACKAGE_DAYS = 5
BASE_PACKAGE_MAX_WEIGHT = 10
ADVANCED_PACKAGE_COST_FACTOR = 5
ADVANCED_PACKAGE_COST_SUPPL = 2
ADVANCED_PACKAGE_DAYS = 2
OVERNIGHT_PACKAGE_COST_FACTOR = 10
OVERNIGHT_PACKAGE_DAYS = 1

class Package(ABC):
    def __init__(self, recipient, address, weight, shipment_date) -> None:
        self.recipient = recipient
        self.address = address
        self.weight = weight
        self.shipment_date = shipment_date

    @abstractmethod
    def calculate_cost(self):
        pass

    @abstractmethod
    def calculate_delivery_time(self):
        pass

    @property
    def recipient(self):
        return self._recipient

    @recipient.setter
    def recipient(self, value):
        self._recipient = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        try:
            self._weight = int(value)
            if int(value) <= 0:
                raise ValueError("Weight must be an integer greater than zero") \
                    from None
        except ValueError:
            raise   

    @property
    def shipment_date(self):
        return self._shipment_date

    @shipment_date.setter
    def shipment_date(self, value):
        try:
            if isinstance(value, str):
                self._shipment_date = datetime.strptime(value, '%Y-%m-%d').date()
            elif isinstance(value, date):
                self._shipment_date = value
        except ValueError:
            raise ValueError("Shipment date must be a valid date") \
                from None

    def __str__(self) -> str:
        return "Recipient: " + self.recipient \
            + "\nAddress: " + self.address \
            + "\nWeight: " + str(self.weight) \
            + "\nShipment date: " + str(self.shipment_date)

class BasePackage(Package):
    def calculate_cost(self):
        return BASE_PACKAGE_COST_FACTOR * self.weight

    def calculate_delivery_time(self):
        if self.weight <= BASE_PACKAGE_MAX_WEIGHT:
            return self.shipment_date + timedelta(days=BASE_PACKAGE_DAYS)
        else:
            return self.shipment_date + timedelta(days=BASE_PACKAGE_DAYS+1)

class AdvancedPackage(Package):
    def calculate_cost(self):
        return ADVANCED_PACKAGE_COST_FACTOR * self.weight + ADVANCED_PACKAGE_COST_SUPPL

    def calculate_delivery_time(self):
        return self.shipment_date + timedelta(days=ADVANCED_PACKAGE_DAYS)

class OvernightPackage(Package):
    def calculate_cost(self):
        return OVERNIGHT_PACKAGE_COST_FACTOR * self.weight

    def calculate_delivery_time(self):
        return self.shipment_date + timedelta(days=OVERNIGHT_PACKAGE_DAYS)


def main():
    #p = Package("aa", "bb", 23, 34)    #not possible
    packages = []
    packages.append(BasePackage("John Doe", "1st Main str.", 3, "2023-01-01"))
    packages.append(AdvancedPackage("Jane Doe", "2nd Wall str.", 23, date.today()))
    packages.append(OvernightPackage("Jack Doe", "3rd Central av.", 12, date.today()))

    for pk in packages:
        print(str(pk))
        print("Estimated delivery time: ", pk.calculate_delivery_time())
        print("Estimated cost: ", pk.calculate_cost())
        print("----")

if __name__ == "__main__":
    main()