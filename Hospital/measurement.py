class Measurement:
    def __init__(self, temp, temp_date) -> None:
        self.temp = temp
        self.temp_date = temp_date

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value

    @property
    def temp_date(self):
        return self._temp_date

    @temp_date.setter
    def temp_date(self, value):
        self._temp_date = value
                
    def __str__(self) -> str:
        return "Date: " + str(self.temp_date) + ", temperature: " + str(self.temp)

    