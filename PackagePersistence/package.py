from abc import ABC, abstractmethod
from datetime import date, datetime

BASE_PACKAGE_COST_FACTOR = 5
BASE_PACKAGE_DAYS = 5
BASE_PACKAGE_MAX_WEIGHT = 10
ADVANCED_PACKAGE_COST_FACTOR = 5
ADVANCED_PACKAGE_COST_SUPPL = 2
ADVANCED_PACKAGE_DAYS = 2
OVERNIGHT_PACKAGE_COST_FACTOR = 10
OVERNIGHT_PACKAGE_DAYS = 1

class Package(ABC):
    def __init__(self, recipient = "", address = "", weight = 0, shipment_date = None) -> None:
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

    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def deserialize(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
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
            if int(value) < 0:
                raise ValueError("Weight must be a positive integer") \
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

