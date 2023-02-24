from datetime import date

class Person:
    def __init__(self, id = 0, name = "", surname = "", birth_year = 0) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

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
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value):
        try:
            self._birth_year = int(value)
            if int(value) < 1900 or int(value) > date.today().year:
                raise ValueError("Birth year must be an integer between 1900 and " \
                    + str(date.today().year)) from None
        except ValueError:
            raise 

    def __str__(self) -> str:
        return "--Person--" \
            + "\nID: " + str(self.id) \
            + "\nName: " + self.name \
            + "\nSurname: " + self.surname \
            + "\nBirth year: " + str(self.birth_year) + "\n"