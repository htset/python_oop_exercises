from abc import ABC, abstractmethod
from datetime import date

class Insurance(ABC):
    def __init__(self, name, birth_year , coverage) -> None:
        self.name = name
        self.birth_year = birth_year
        self.coverage = coverage

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value):
        try:
            self._birth_year= int(value)
            if int(value) < 1900 or int(value) > date.today().year:
                raise ValueError("Birth year must be an integer between 1900 and " \
                    + str(date.today().year)) from None
        except ValueError:
            raise 

    @property
    def coverage(self):
        return self._coverage

    @coverage.setter
    def coverage(self, value):
        self._coverage = value

    def get_age(self):
        return date.today().year - self.birth_year

    @abstractmethod
    def calculate_cost(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class LifeInsurance(Insurance):
    def calculate_cost(self):
        return 10 * self.get_age() + 0.001 * self.coverage

    def __str__(self):
        return "------Life Insurance policy------" \
            + "\nName: " + self.name \
            + "\nAge: " + str(self.get_age()) \
            + "\nCoverage: " + str(self.coverage) \
            + "\nYearly cost: " + str(self.calculate_cost()) + "\n"

class AutoInsurance(Insurance):
    def __init__(self, name, birth_year , coverage, circulation_year) -> None:
        super().__init__(name, birth_year, coverage)
        self.circulation_year = circulation_year

    @property
    def circulation_year(self):
        return self._circulation_year

    @circulation_year.setter
    def circulation_year(self, value):
        try:
            self._circulation_year= int(value)
            if int(value) < 1900 or int(value) > date.today().year:
                raise ValueError("Circulation year must be an integer between 1900 and " \
                    + str(date.today().year)) from None
        except ValueError:
            raise 

    def get_car_age(self):
        return date.today().year - self.circulation_year

    def calculate_cost(self):
        return -self.get_age() + 0.05 * self.coverage + 10 * self.get_car_age()

    def __str__(self):
        return "------Auto Insurance policy------" \
            + "\nName: " + self.name \
            + "\nAge: " + str(self.get_age()) \
            + "\nCoverage: " + str(self.coverage) \
            + "\nCar age: " + str(self.get_car_age()) \
            + "\nYearly cost: " + str(self.calculate_cost()) + "\n" 


def saveInsurance(insurance):
    file = open("insurance.txt", "a")
    file.write(str(insurance))

def main():
    i1 = AutoInsurance("John Doe", 2000, 15000, 2010)
    print(i1)
    i2 = LifeInsurance("John Doe", 2000, 1000000)
    print(i2)

    saveInsurance(i1)
    saveInsurance(i2)

if __name__ == "__main__":
    main()