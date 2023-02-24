import datetime

class Reservation:
    def __init__(self, id = 0, name = "", surname = "", start_date = 0, \
    duration = 0, cost = 0) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.start_date = start_date
        self.duration = duration
        self.cost = cost
        self.persons = []

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
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        try:
            if isinstance(value, str):
                self._start_date = datetime.strptime(value, '%Y-%m-%d').date()
            elif isinstance(value, datetime.date):
                self._start_date = value
        except ValueError:
            raise ValueError("Start date date must be a valid date") \
                from None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        try:
            self._duration = int(value)
            if int(value) < 0:
                raise ValueError("Duration must be an integer >= 0 ")
        except ValueError:
            raise

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        try:
            self._cost = int(value)
            if int(value) < 0:
                raise ValueError("Cost must be an integer >= 0 ")
        except ValueError:
            raise

    @property
    def persons(self):
        return self._persons

    @persons.setter
    def persons(self, value):
        self._persons = value

    def __str__(self) -> str:
        temp_str = "-----Reservation details-----\n" \
            + "--Apartment--" \
            + "\nID: " + str(self.id) \
            + "\nName: " + self.name \
            + "\nSurname: " + self.surname \
            + "\nStart date: " + str(self.start_date) \
            + "\nDuration: " + str(self.duration) \
            + "\nTotal Cost: " + str(self.cost) \
            + "\nPersons: " + "\n\n"
        
        for p in self.persons:
            temp_str = temp_str + str(p) + "\n"

        return temp_str

    def add_person(self, person):
        self.persons.append(person)

    def get_checkout_date(self):
        return self.start_date + datetime.timedelta(days=self.duration)

