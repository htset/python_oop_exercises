from measurement import Measurement
from datetime import datetime, date
from multipledispatch import dispatch

class Patient:
    def __init__(self, name, surname, year_of_birth, clinic, room) -> None:
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth
        self.clinic = clinic
        self.room = room
        self.measurements = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def year_of_birth(self):
        return self._year_of_birth

    @year_of_birth.setter
    def year_of_birth(self, value):
        try:
            self._year_of_birth = int(value)
            if int(value) < 1900 or int(value) > date.today().year:
                raise ValueError("Duration must be an integer between 1900 and " \
                    + str(date.today().year)) from None
        except ValueError:
            raise 

    @property
    def clinic(self):
        return self._clinic

    @clinic.setter
    def clinic(self, value):
        self._clinic = value

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, value):
        self._room = value

    @property
    def measurements(self):
        return self._measurements

    @measurements.setter
    def measurements(self, value):
        self._measurements = value

    @dispatch(Measurement)
    def insert_measurement(self, m):
        self.measurements.append(m)

    @dispatch(float, datetime)
    def insert_measurement(self, temp, temp_date):
        m = Measurement(temp, temp_date)
        self.measurements.append(m)

    def max_temp(self):
        max = 0
        for m in self.measurements:
            if m.temp > max:
                max = m.temp
        return max

    def get_age(self):
        return date.today().year - self.year_of_birth

    def __str__(self) -> str:
        temp_str = "-----Patient info: ------" \
            + "\nName: " + self.name + " " + self.surname \
            + "\nBirth year: " + str(self.year_of_birth) \
            + "\nRoom: " + self.room \
            + "\nMeasurements: " 

        for m in self.measurements:
            temp_str = temp_str + "\n" + str(m)

        temp_str = temp_str + "\nClinic: " + str(self.clinic)
        return temp_str

