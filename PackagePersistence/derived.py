from package import Package, BASE_PACKAGE_COST_FACTOR, BASE_PACKAGE_DAYS, \
    BASE_PACKAGE_MAX_WEIGHT, ADVANCED_PACKAGE_COST_FACTOR, \
    ADVANCED_PACKAGE_COST_SUPPL, ADVANCED_PACKAGE_DAYS, \
    OVERNIGHT_PACKAGE_COST_FACTOR, OVERNIGHT_PACKAGE_DAYS
from datetime import timedelta, datetime

class BasePackage(Package):
    def calculate_cost(self):
        return BASE_PACKAGE_COST_FACTOR * self.weight

    def calculate_delivery_time(self):
        if self.weight <= BASE_PACKAGE_MAX_WEIGHT:
            return self.shipment_date + timedelta(days=BASE_PACKAGE_DAYS)
        else:
            return self.shipment_date + timedelta(days=BASE_PACKAGE_DAYS+1)

    def serialize(self):
        return "BasePackage" \
            + "\n" + self.recipient \
            + "\n" + self.address \
            + "\n" + str(self.weight) \
            + "\n" + str(self.shipment_date) \
            + "\n---\n"

    def deserialize(self, str):
        list = str.split("\n")
        self.recipient = list[1]
        self.address =  list[2]
        self.weight = int(list[3])
        self.shipment_date = datetime.strptime(list[4], '%Y-%m-%d').date()

    def __str__(self) -> str:
        return "Base package" \
            + "\nRecipient: " + self.recipient \
            + "\nAddress: " + self.address \
            + "\nWeight: " + str(self.weight) \
            + "\nShipment date: " + str(self.shipment_date)

class AdvancedPackage(Package):
    def calculate_cost(self):
        return ADVANCED_PACKAGE_COST_FACTOR * self.weight + ADVANCED_PACKAGE_COST_SUPPL

    def calculate_delivery_time(self):
        return self.shipment_date + timedelta(days=ADVANCED_PACKAGE_DAYS)

    def serialize(self):
        return "AdvancedPackage" \
            + "\n" + self.recipient \
            + "\n" + self.address \
            + "\n" + str(self.weight) \
            + "\n" + str(self.shipment_date) \
            + "\n---\n"

    def deserialize(self, str):
        list = str.split("\n")
        self.recipient = list[1]
        self.address =  list[2]
        self.weight = int(list[3])
        self.shipment_date = datetime.strptime(list[4], '%Y-%m-%d').date()

    def __str__(self) -> str:
        return "Advanced package" \
            + "\nRecipient: " + self.recipient \
            + "\nAddress: " + self.address \
            + "\nWeight: " + str(self.weight) \
            + "\nShipment date: " + str(self.shipment_date)

class OvernightPackage(Package):
    def calculate_cost(self):
        return OVERNIGHT_PACKAGE_COST_FACTOR * self.weight

    def calculate_delivery_time(self):
        return self.shipment_date + timedelta(days=OVERNIGHT_PACKAGE_DAYS)

    def serialize(self):
        return "OvernightPackage" \
            + "\n" + self.recipient \
            + "\n" + self.address \
            + "\n" + str(self.weight) \
            + "\n" + str(self.shipment_date) \
            + "\n---\n"

    def deserialize(self, str):
        list = str.split("\n")
        self.recipient = list[1]
        self.address =  list[2]
        self.weight = int(list[3])
        self.shipment_date = datetime.strptime(list[4], '%Y-%m-%d').date()

    def __str__(self) -> str:
        return "Overnight package" \
            + "\nRecipient: " + self.recipient \
            + "\nAddress: " + self.address \
            + "\nWeight: " + str(self.weight) \
            + "\nShipment date: " + str(self.shipment_date)
